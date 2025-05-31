import io
import os
import pathlib
from typing import Any

import ndspy.rom

from dqmj1_util.raw.btl_enmy_prm import BtlEnmyPrm
from dqmj1_util.regions import Region

BTL_ENMY_PRM_PATH = "BtlEnmyPrm.bin"


class Rom:
    def __init__(
        self, filepath: os.PathLike[Any] | str, region: Region = Region.NorthAmerica
    ) -> None:
        self.filepath = pathlib.Path(filepath)
        self.region = region

        self.rom = ndspy.rom.NintendoDSRom.fromFile(self.filepath)

    def load_btl_enmy_prm(self) -> BtlEnmyPrm:
        data = self.rom.getFileByName(BTL_ENMY_PRM_PATH)

        input_stream = io.BytesIO(data)
        return BtlEnmyPrm.from_bin(input_stream)
