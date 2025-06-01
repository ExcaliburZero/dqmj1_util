from __future__ import annotations

from dataclasses import dataclass

import ndspy.rom

from dqmj1_util.regions import Region
from dqmj1_util.string_tables.locations import STRING_TABLE_LOCATIONS


@dataclass
class StringTables:
    species_names: list[str]

    @staticmethod
    def from_rom(rom: ndspy.rom.NintendoDSRom, region: Region) -> StringTables:
        string_table_locations = STRING_TABLE_LOCATIONS[region]

        return StringTables(species_names=string_table_locations.species_names.read(rom, region))
