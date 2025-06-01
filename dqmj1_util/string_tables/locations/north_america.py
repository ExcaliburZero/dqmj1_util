from dqmj1_util.string_tables.locations.locations import StringTableLocations, TableLocation

NORTH_AMERICA_STRING_TABLE_LOCATIONS = StringTableLocations(
    species_names=TableLocation("arm9.bin", 0x207785C, 0x207805C),
    skill_names=TableLocation("arm9.bin", 0x2076BE8, 0x207705C),
    skill_set_names=TableLocation("arm9.bin", 0x20763E0, 0x20767E4),
    item_names=TableLocation("arm9.bin", 0x20767E4, 0x2076BE8),
)
