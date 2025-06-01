from dqmj1_util.string_tables import StringTables

STRING_TABLES = StringTables(
    species_names=[f"species_{i}" for i in range(0, 512)],
    skill_names=[f"skill_{i}" for i in range(0, 285)],
    skill_set_names=[f"skill_set_{i}" for i in range(0, 257)],
    item_names=[f"item_{i}" for i in range(0, 257)],
)
