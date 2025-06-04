from __future__ import annotations

from dataclasses import dataclass

from dqmj1_util._string_tables import StringTables


@dataclass
class Skill:
    name: str

    @staticmethod
    def from_raw(skill_id: int, string_tables: StringTables) -> Skill:
        params = {}

        # TODO: add the likely many more parameters

        params["name"] = string_tables.skill_names[skill_id]

        return Skill(**params)
