from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from dqmj1_util._string_tables import StringTables
from dqmj1_util.raw._skill_tbl import SkillTblEntryJp, SkillTblEntryNaEu


@dataclass
class SkillSet:
    name: str
    can_upgrade: bool
    category: int  # TODO: make into an enum
    max_skill_points: int
    rewards: list[Reward]
    species_learnt_by: list[str]
    species_learnt_by_ids: list[int]

    @dataclass
    class Reward:
        skill_point_requirement: int
        skill: Optional[str]
        skill_id: Optional[int]
        trait: Optional[str]
        trait_id: Optional[int]

    @staticmethod
    def from_raw(
        skill_set_id: int, raw: SkillTblEntryJp | SkillTblEntryNaEu, string_tables: StringTables
    ) -> SkillSet:
        params = vars(raw)
        params = {key: value for key, value in params.items() if not key.startswith("unknown")}

        params["name"] = string_tables.skill_set_names[skill_set_id]
        params["can_upgrade"] = raw.can_upgrade > 0
        params["species_learnt_by_ids"] = []

        rewards: list[SkillSet.Reward] = []
        for i in range(0, raw.num_rewards):
            skill = None
            skill_id = None
            trait = None
            trait_id = None

            if len(raw.skills[i]) > 0:
                skill_id = raw.skills[i].skill_ids[0]
                skill = string_tables.skill_names[skill_id]

            if len(raw.traits[i]) > 0:
                trait_id = raw.traits[i].trait_ids[0]
                trait = string_tables.trait_names[trait_id]

            rewards.append(
                SkillSet.Reward(
                    skill_point_requirement=raw.skill_point_requirements[i].points_total,
                    skill=skill,
                    skill_id=skill_id,
                    trait=trait,
                    trait_id=trait_id,
                )
            )
        params["rewards"] = rewards

        keys_to_keep = [
            "name",
            "can_upgrade",
            "category",
            "max_skill_points",
            "rewards",
            "species_learnt_by",
            "species_learnt_by_ids",
        ]
        params = {key: value for key, value in params.items() if key in keys_to_keep}

        return SkillSet(**params)
