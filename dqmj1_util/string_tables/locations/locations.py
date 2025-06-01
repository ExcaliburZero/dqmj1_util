from dataclasses import dataclass
from typing import Literal

import ndspy.rom

from dqmj1_util.character_encoding import CHARACTER_ENCODINGS
from dqmj1_util.region import Region

ENDIANESS: Literal["little"] = "little"

POINTER_SIZE = 4
FILE_OFFSETS = {"arm9.bin": 0x02000000}


@dataclass
class TableLocation:
    filepath: str
    start: int
    end: int

    def read(
        self, rom: ndspy.rom.NintendoDSRom, region: Region, max_string_length: int = 100
    ) -> list[str]:
        offset = FILE_OFFSETS[self.filepath]
        character_encoding = CHARACTER_ENCODINGS[region]

        start = self.start - offset
        end = self.end - offset

        if self.filepath == "arm9.bin":
            data = rom.arm9
        else:
            raise ValueError(self.filepath)

        string_pointers = []
        current = start
        while current < end:
            string_pointers.append(
                int.from_bytes(data[current : current + POINTER_SIZE], ENDIANESS)
            )

            current += POINTER_SIZE

        strings = []
        for string_pointer in string_pointers:
            string_pointer -= offset

            strings.append(
                character_encoding.read_string(
                    data[string_pointer : string_pointer + max_string_length]
                )
            )

        return strings


@dataclass
class StringTableLocations:
    species_names: TableLocation
    skill_names: TableLocation
    trait_names: TableLocation
    skill_set_names: TableLocation
    item_names: TableLocation
