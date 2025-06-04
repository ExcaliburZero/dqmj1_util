from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import TypeVar

from dqmj1_util._string_tables import StringTables
from dqmj1_util.raw._btl_enmy_prm import BtlEnmyPrmEntry

T = TypeVar("T")


@dataclass
class Encounter:
    species: str
    species_id: int
    skills: list[str]
    skill_ids: list[int]
    item_drops: list[str]
    item_drop_item_ids: list[int]
    gold: int
    exp: int
    level: int
    scout_chance: int
    max_hp: int
    max_mp: int
    attack: int
    defense: int
    agility: int
    wisdom: int
    skill_sets: list[str]
    skill_set_ids: list[int]

    @staticmethod
    def from_raw(raw: BtlEnmyPrmEntry, string_tables: StringTables) -> Encounter:
        params = vars(raw)
        params = {key: value for key, value in params.items() if not key.startswith("unknown")}

        raw_skills = Encounter._unique_objects(raw.skills)
        raw_skill_set_ids = [
            skill_set_id
            for skill_set_id in Encounter._unique_values(raw.skill_set_ids)
            if skill_set_id != 0
        ]
        raw_item_drops = [item_drop for item_drop in raw.item_drops if item_drop.item_id != 0]

        params["species"] = string_tables.species_names[raw.species_id]
        params["skills"] = [string_tables.skill_names[skill.skill_id] for skill in raw_skills]
        params["skill_ids"] = [skill.skill_id for skill in raw_skills]
        params["skill_sets"] = [
            string_tables.skill_set_names[skill_set_id] for skill_set_id in raw_skill_set_ids
        ]
        params["skill_set_ids"] = raw_skill_set_ids.copy()
        params["item_drops"] = [
            f"{string_tables.item_names[item_drop.item_id]} {(1.0 / 2**item_drop.chance_denominator_2_power) * 100.0}%"
            for item_drop in raw_item_drops
        ]
        params["item_drop_item_ids"] = [item_drop.item_id for item_drop in raw_item_drops]

        return Encounter(**params)

    @staticmethod
    def _unique_objects(l: Iterable[T]) -> list[T]:
        """
        Returns only the unique items in the given iterable. Specifically preserves order.
        """
        output_list = []
        found = []
        for e in l:
            key = vars(e)

            if key in found:
                continue

            found.append(key)
            output_list.append(e)

        return output_list

    @staticmethod
    def _unique_values(l: Iterable[T]) -> list[T]:
        """
        Returns only the unique items in the given iterable. Specifically preserves order.
        """
        output_list = []
        found = set()
        for e in l:
            if e in found:
                continue

            found.add(e)
            output_list.append(e)

        return output_list
