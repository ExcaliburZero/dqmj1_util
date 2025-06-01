import io
import os
import pathlib
from typing import Any, Optional

import ndspy.rom

from dqmj1_util.raw.btl_enmy_prm import BtlEnmyPrm
from dqmj1_util.raw.skill_tbl import SkillTbl
from dqmj1_util.region import Region
from dqmj1_util.simple.encounter import Encounter
from dqmj1_util.simple.skill_set import SkillSet
from dqmj1_util.string_tables import StringTables

BTL_ENMY_PRM_PATH = "BtlEnmyPrm.bin"
SKILL_TBL_PATH = "SkillTbl.bin"


class Rom:
    def __init__(
        self, filepath: os.PathLike[Any] | str, region: Region = Region.NorthAmerica
    ) -> None:
        self.filepath = pathlib.Path(filepath)
        self.region = region

        self.rom = ndspy.rom.NintendoDSRom.fromFile(self.filepath)

        self._string_tables: Optional[StringTables] = None

    @property
    def string_tables(self) -> StringTables:
        if self._string_tables is not None:
            return self._string_tables

        self._string_tables = StringTables.from_rom(self.rom, self.region)
        return self._string_tables

    def load_btl_enmy_prm(self) -> BtlEnmyPrm:
        data = self.rom.getFileByName(BTL_ENMY_PRM_PATH)

        input_stream = io.BytesIO(data)
        return BtlEnmyPrm.from_bin(input_stream)

    def load_skill_tbl(self) -> SkillTbl:
        data = self.rom.getFileByName(SKILL_TBL_PATH)

        input_stream = io.BytesIO(data)
        return SkillTbl.from_bin(input_stream, self.region)

    def load_encounters(self) -> list[Encounter]:
        btl_enmy_prm = self.load_btl_enmy_prm()

        return [Encounter.from_raw(entry, self.string_tables) for entry in btl_enmy_prm.entries]

    def load_skill_sets(self) -> list[SkillSet]:
        skill_tbl = self.load_skill_tbl()

        return [
            SkillSet.from_raw(i, entry, self.string_tables)
            for i, entry in enumerate(skill_tbl.entries)
        ]
