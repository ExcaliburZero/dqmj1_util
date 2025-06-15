from dqmj1_util._string_tables._locations._locations import StringTableLocations, TableLocation

JAPAN_STRING_TABLE_LOCATIONS = StringTableLocations(
    species_names=TableLocation("arm9.bin", 0x0208E8E8, 0x0208F0E8),
    skill_names=TableLocation(
        "arm9.bin", 0x0208DCE0, 0x208E27C
    ),  # Not correct end location, but includes all the needed strings
    trait_names=TableLocation("arm9.bin", 0x0208C8D8, 0x0208CCD8),
    skill_set_names=TableLocation("arm9.bin", 0x0208D4D8, 0x0208D8DC),
    item_names=TableLocation("arm9.bin", 0x0208D8DC, 0x0208DCE0),
)
