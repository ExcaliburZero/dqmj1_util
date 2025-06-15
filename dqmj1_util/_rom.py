from __future__ import annotations

import copy
import io
import os
import pathlib
from collections.abc import Iterable
from typing import Any, Callable, Generic, Optional, TypeVar, cast

import ndspy.rom

from dqmj1_util._region import Region
from dqmj1_util._string_tables import StringTables
from dqmj1_util.raw._btl_enmy_prm import BtlEnmyPrm
from dqmj1_util.raw._skill_tbl import SkillTbl, SkillTblEntryJp, SkillTblEntryNaEu
from dqmj1_util.simple._encounter import Encounter
from dqmj1_util.simple._skill import Skill
from dqmj1_util.simple._skill_set import SkillSet

BTL_ENMY_PRM_PATH = "BtlEnmyPrm.bin"
SKILL_TBL_PATH = "SkillTbl.bin"

T = TypeVar("T")


class CachedData(Generic[T]):
    """
    Utility class for cacheable data. Only loads data on request and marks data as dirty if it
    is modified. Supports both read only and read/writeable data.

    Tracks "children" (data that is derived from this data) to automatically clear them when
    the parent data is written to.

    Designed assuming that writeable data will not be a child of any other writeable data.
    """

    def __init__(
        self,
        load_function: Callable[[], T],
        writeable: bool = False,
        children: Optional[Iterable[CachedData[Any]]] = None,
    ) -> None:
        self._load_function = load_function
        self._is_writable = writeable
        self._children = list(children) if children is not None else []

        self._data: Optional[T] = None
        self._is_dirty = False

        for child in self._children:
            if child.is_writeable:
                raise RuntimeError

    @property
    def is_writeable(self) -> bool:
        return self._is_writable

    @property
    def is_dirty(self) -> bool:
        return self._is_dirty

    def mark_dirty(self) -> None:
        self._is_dirty = True

        for child in self._children:
            child.clear()

    def mark_clean(self) -> None:
        self._is_dirty = False

    def clear(self) -> None:
        self._is_dirty = False
        self._data = None

    def set(self, value: T) -> None:
        if not self.is_writeable:
            raise RuntimeError

        self.mark_dirty()
        self._data = value

    def get(self) -> T:
        if self._data is None:
            self._data = self._load_function()

        # Always do a deep copy, because if the data is mutable then modifying it directly would
        # bypass the dirty marker
        return copy.deepcopy(self._data)


class Rom:
    """
    ROM containing the game's internal binaries and data files.

    Used to read data from and write data to the game ROM.
    """

    def __init__(
        self, filepath: os.PathLike[Any] | str, region: Region = Region.NorthAmerica
    ) -> None:
        """
        Create a ROM object from the filepath to the ROM file.

        If not using a North American ROM file, you must provide the region the ROM is from.

        :param filepath: Filepath to the ROM file to work with.
        :param region: Region the ROM file is for.
        """
        self._filepath = pathlib.Path(filepath)
        self._region = region

        self._rom = ndspy.rom.NintendoDSRom.fromFile(self._filepath)

        self._encounters = CachedData(self._load_encounters)
        self._skill_sets = CachedData(self._load_skill_sets)
        self._skills = CachedData(self._load_skills)

        self._btl_enmy_prm = CachedData(
            self._load_btl_enmy_prm, writeable=True, children=[self._encounters]
        )
        self._skill_tbl = CachedData(
            self._load_skill_tbl, writeable=True, children=[self._skill_sets]
        )

        self._string_tables = CachedData(
            self._load_string_tables,
            children=[self._encounters, self._skill_sets, self._skills],
        )

    def __repr__(self) -> str:
        return f"Rom(filepath={self._filepath}, region={self._region})"

    @property
    def filepath(self) -> pathlib.Path:
        """
        Filepath the ROM was read from.
        """
        return self._filepath

    @property
    def region(self) -> Region:
        """
        Region the rom is for (North America, Europe, Japan).

        Based on the region that was provided to the constructor.
        """
        return self._region

    @property
    def rom(self) -> ndspy.rom.NintendoDSRom:
        """
        Instance of the :class:`ndspy.rom.NintendoDSRom` object this class uses to
        read/modify/write the game's ROM.

        Can be mutated in order to apply custom changes to the game's code and data files.
        """
        return self._rom

    def write(self, filepath: os.PathLike[Any] | str) -> None:
        """
        Writes the ROM (with any applied modifications) to the given filepath.

        Make sure you have applied any modifications you want to make prior to calling this method.
        You can do that by assigning modified data to properties like :attr:`~Rom.btl_enmy_prm` or
        :attr:`~Rom.skill_tbl`.
        """
        if self._btl_enmy_prm.is_dirty:
            output_stream = io.BytesIO()
            self.btl_enmy_prm.write_bin(output_stream)
            self._rom.setFileByName(BTL_ENMY_PRM_PATH, bytes(output_stream.getbuffer()))

        if self._skill_tbl.is_dirty:
            raise NotImplementedError

        self._rom.saveToFile(filepath)

    def _load_string_tables(self) -> StringTables:
        return StringTables.from_rom(self._rom, self._region)

    def _load_btl_enmy_prm(self) -> BtlEnmyPrm:
        data = self._rom.getFileByName(BTL_ENMY_PRM_PATH)

        input_stream = io.BytesIO(data)
        return BtlEnmyPrm.from_bin(input_stream)

    def _load_encounters(self) -> list[Encounter]:
        return [
            Encounter.from_raw(entry, self.string_tables) for entry in self.btl_enmy_prm.entries
        ]

    def _load_skill_tbl(self) -> SkillTbl:
        data = self._rom.getFileByName(SKILL_TBL_PATH)

        input_stream = io.BytesIO(data)
        return SkillTbl.from_bin(input_stream, self._region)

    def _load_skill_sets(self) -> list[SkillSet]:
        return [
            SkillSet.from_raw(
                i, cast("SkillTblEntryJp | SkillTblEntryNaEu", entry), self.string_tables
            )
            for i, entry in enumerate(self.skill_tbl.entries)
        ]

    def _load_skills(self) -> list[Skill]:
        return [Skill.from_raw(i, self.string_tables) for i in range(0, 285)]

    @property
    def string_tables(self) -> StringTables:
        """
        String tables stored in the ROM's binaries.

        Read-only, no read/write interface currently.
        """
        return self._string_tables.get()

    @property
    def btl_enmy_prm(self) -> BtlEnmyPrm:
        """
        Encounters table containing data on monsters encountered in battles, received as gifts, or
        obtained as starters.

        Read and write
        """
        return self._btl_enmy_prm.get()

    @btl_enmy_prm.setter
    def btl_enmy_prm(self, value: BtlEnmyPrm) -> None:
        self._btl_enmy_prm.set(value)

    @property
    def encounters(self) -> list[Encounter]:
        """
        Encounters table containing data on monsters encountered in battles, received as gifts, or
        obtained as starters.

        Read-only, to write/modify use :attr:`~Rom.btl_enmy_prm` instead.
        """
        return self._encounters.get()

    @property
    def skill_tbl(self) -> SkillTbl:
        """
        Skill sets that reward monsters with skill and/or traits as they allocate skill points.

        Read and write
        """
        return self._skill_tbl.get()

    @skill_tbl.setter
    def skill_tbl(self, value: SkillTbl) -> None:
        self._skill_tbl.set(value)

    @property
    def skill_sets(self) -> list[SkillSet]:
        """
        Skill sets that reward monsters with skill and/or traits as they allocate skill points.

        Read-only, to write/modify use :attr:`~Rom.skill_tbl` instead.
        """
        return self._skill_sets.get()

    @property
    def skills(self) -> list[Skill]:
        """
        Skills that monsters can obtain and use in battle.

        Read-only, no read/write interface currently.
        """
        return self._skills.get()
