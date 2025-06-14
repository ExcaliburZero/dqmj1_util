import unittest

from dqmj1_util.raw._btl_enmy_prm import (
    BtlEnmyPrmEntry,
)
from dqmj1_util.simple._encounter import Encounter
from tests.util import STRING_TABLES


class TestEncounter(unittest.TestCase):
    def test_from_raw_simple(self) -> None:
        raw = BtlEnmyPrmEntry(
            species_id=1,
            unknown_a=b"\x00\x00\x00\x00\x00\x00",
            skills=[
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 1),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 2),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 3),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 4),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 5),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 6),
            ],
            item_drops=[
                BtlEnmyPrmEntry.ItemDrop(1, 0),
                BtlEnmyPrmEntry.ItemDrop(2, 7),
            ],
            gold=288,
            unknown_b=b"\x00\x00",
            exp=2,
            unknown_c=b"\x00\x00",
            level=16,
            unknown_d=b"\x00",
            unknown_e=b"\x00",
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            unknown_f=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            skill_set_ids=[1, 2, 3],
            unknown_g=b"\x00",
        )

        expected = Encounter(
            species="species_1",
            species_id=1,
            skills=["skill_1", "skill_2", "skill_3", "skill_4", "skill_5", "skill_6"],
            skill_ids=[1, 2, 3, 4, 5, 6],
            item_drops=["item_1 100.0%", "item_2 0.78125%"],
            item_drop_item_ids=[1, 2],
            gold=288,
            exp=2,
            level=16,
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            skill_sets=["skill_set_1", "skill_set_2", "skill_set_3"],
            skill_set_ids=[1, 2, 3],
        )
        actual = Encounter.from_raw(raw, STRING_TABLES)

        self.assertEqual(expected, actual)

    def test_from_raw_repeat_skill(self) -> None:
        raw = BtlEnmyPrmEntry(
            species_id=1,
            unknown_a=b"\x00\x00\x00\x00\x00\x00",
            skills=[
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 1),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 2),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 3),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 2),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 5),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 6),
            ],
            item_drops=[
                BtlEnmyPrmEntry.ItemDrop(1, 0),
                BtlEnmyPrmEntry.ItemDrop(2, 7),
            ],
            gold=288,
            unknown_b=b"\x00\x00",
            exp=2,
            unknown_c=b"\x00\x00",
            level=16,
            unknown_d=b"\x00",
            unknown_e=b"\x00",
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            unknown_f=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            skill_set_ids=[1, 2, 3],
            unknown_g=b"\x00",
        )

        expected = Encounter(
            species="species_1",
            species_id=1,
            skills=["skill_1", "skill_2", "skill_3", "skill_5", "skill_6"],
            skill_ids=[1, 2, 3, 5, 6],
            item_drops=["item_1 100.0%", "item_2 0.78125%"],
            item_drop_item_ids=[1, 2],
            gold=288,
            exp=2,
            level=16,
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            skill_sets=["skill_set_1", "skill_set_2", "skill_set_3"],
            skill_set_ids=[1, 2, 3],
        )
        actual = Encounter.from_raw(raw, STRING_TABLES)

        self.assertEqual(expected, actual)

    def test_from_raw_repeat_skill_set(self) -> None:
        raw = BtlEnmyPrmEntry(
            species_id=1,
            unknown_a=b"\x00\x00\x00\x00\x00\x00",
            skills=[
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 1),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 2),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 3),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 4),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 5),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 6),
            ],
            item_drops=[
                BtlEnmyPrmEntry.ItemDrop(1, 0),
                BtlEnmyPrmEntry.ItemDrop(2, 7),
            ],
            gold=288,
            unknown_b=b"\x00\x00",
            exp=2,
            unknown_c=b"\x00\x00",
            level=16,
            unknown_d=b"\x00",
            unknown_e=b"\x00",
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            unknown_f=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            skill_set_ids=[1, 2, 1],
            unknown_g=b"\x00",
        )

        expected = Encounter(
            species="species_1",
            species_id=1,
            skills=["skill_1", "skill_2", "skill_3", "skill_4", "skill_5", "skill_6"],
            skill_ids=[1, 2, 3, 4, 5, 6],
            item_drops=["item_1 100.0%", "item_2 0.78125%"],
            item_drop_item_ids=[1, 2],
            gold=288,
            exp=2,
            level=16,
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            skill_sets=["skill_set_1", "skill_set_2"],
            skill_set_ids=[1, 2],
        )
        actual = Encounter.from_raw(raw, STRING_TABLES)

        self.assertEqual(expected, actual)

    def test_from_raw_empty_item_drop(self) -> None:
        raw = BtlEnmyPrmEntry(
            species_id=1,
            unknown_a=b"\x00\x00\x00\x00\x00\x00",
            skills=[
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 1),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 2),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 3),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 4),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 5),
                BtlEnmyPrmEntry.EnemySkill(b"\x00\x00", 6),
            ],
            item_drops=[
                BtlEnmyPrmEntry.ItemDrop(0, 0),
                BtlEnmyPrmEntry.ItemDrop(2, 7),
            ],
            gold=288,
            unknown_b=b"\x00\x00",
            exp=2,
            unknown_c=b"\x00\x00",
            level=16,
            unknown_d=b"\x00",
            unknown_e=b"\x00",
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            unknown_f=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
            skill_set_ids=[1, 2, 3],
            unknown_g=b"\x00",
        )

        expected = Encounter(
            species="species_1",
            species_id=1,
            skills=["skill_1", "skill_2", "skill_3", "skill_4", "skill_5", "skill_6"],
            skill_ids=[1, 2, 3, 4, 5, 6],
            item_drops=["item_2 0.78125%"],
            item_drop_item_ids=[2],
            gold=288,
            exp=2,
            level=16,
            scout_chance=5,
            max_hp=5,
            max_mp=6,
            attack=7,
            defense=8,
            agility=9,
            wisdom=10,
            skill_sets=["skill_set_1", "skill_set_2", "skill_set_3"],
            skill_set_ids=[1, 2, 3],
        )
        actual = Encounter.from_raw(raw, STRING_TABLES)

        self.assertEqual(expected, actual)
