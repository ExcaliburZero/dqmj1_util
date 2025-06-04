from dqmj1_util._string_tables import StringTables
from dqmj1_util.simple._encounter import Encounter
from dqmj1_util.simple._skill import Skill
from dqmj1_util.simple._skill_set import SkillSet

STRING_TABLES = StringTables(
    species_names=[f"species_{i}" for i in range(0, 512)],
    skill_names=[f"skill_{i}" for i in range(0, 285)],
    trait_names=[f"trait_{i}" for i in range(0, 256)],
    skill_set_names=[f"skill_set_{i}" for i in range(0, 257)],
    item_names=[f"item_{i}" for i in range(0, 257)],
)

SKILLS = [Skill(name=f"skill_{i}") for i in range(0, 285)]
SKILL_SETS = [
    SkillSet(
        name=f"skill_{i}",
        can_upgrade=False,
        category=1,
        max_skill_points=100,
        rewards=[],
        species_learnt_by=["species_a"],
        species_learnt_by_ids=[2],
    )
    for i in range(0, 257)
]
ENCOUNTERS = [
    Encounter(
        species="species_a",
        species_id=1,
        skills=["skill_b"],
        skill_ids=[2],
        item_drops=["item_c"],
        item_drop_item_ids=[3],
        gold=100,
        exp=150,
        level=30,
        scout_chance=100,
        max_hp=25,
        max_mp=13,
        attack=5,
        defense=6,
        agility=7,
        wisdom=9,
        skill_sets=["skill_set_d"],
        skill_set_ids=[5],
    )
    for _ in range(0, 257)
]
