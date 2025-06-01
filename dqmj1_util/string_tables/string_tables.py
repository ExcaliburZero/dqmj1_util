from __future__ import annotations

from dataclasses import dataclass

import ndspy.rom

from dqmj1_util.regions import Region
from dqmj1_util.string_tables.locations import STRING_TABLE_LOCATIONS


@dataclass
class StringTables:
    species_names: list[str]
    skill_names: list[str]
    skill_set_names: list[str]
    item_names: list[str]

    @staticmethod
    def from_rom(rom: ndspy.rom.NintendoDSRom, region: Region) -> StringTables:
        string_table_locations = STRING_TABLE_LOCATIONS[region]

        tables = {
            name: table.read(rom, region) for name, table in vars(string_table_locations).items()
        }

        return StringTables(**tables)
