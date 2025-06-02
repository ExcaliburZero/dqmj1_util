from __future__ import annotations

from dataclasses import dataclass

import ndspy.rom

from dqmj1_util.region import Region
from dqmj1_util.string_tables.locations import STRING_TABLE_LOCATIONS


@dataclass
class StringTables:
    """
    Tables of strings stored in the ROM's binaries.

    Used for looking up the names of monster species, skills, traits, etc. based on their id number.
    """

    species_names: list[str]
    skill_names: list[str]
    trait_names: list[str]
    skill_set_names: list[str]
    item_names: list[str]

    @staticmethod
    def from_rom(rom: ndspy.rom.NintendoDSRom, region: Region) -> StringTables:
        """
        Reads StringTables from the given ROM.

        The locations in the binaries that the string tables are read from is dependant on the
        provided region.

        Generally you don't need to call this directly, as :class:`Rom` calls it as a part of
        :attr:`Rom.string_tables`.

        :param rom: ROM to read string tables from.
        :param region: Region the ROM is for.
        """
        string_table_locations = STRING_TABLE_LOCATIONS[region]

        tables = {
            name: table.read(rom, region) for name, table in vars(string_table_locations).items()
        }

        return StringTables(**tables)
