import io
import os
import pathlib
from typing import Any, Optional

import ndspy.rom

from dqmj1_util.raw.btl_enmy_prm import BtlEnmyPrm
from dqmj1_util.regions import Region
from dqmj1_util.simple.encounters import Encounter
from dqmj1_util.string_tables import StringTables

BTL_ENMY_PRM_PATH = "BtlEnmyPrm.bin"


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

    def load_encounters(self) -> list[Encounter]:
        btl_enmy_prm = self.load_btl_enmy_prm()

        return [Encounter.from_raw(entry, self.string_tables) for entry in btl_enmy_prm.entries]
