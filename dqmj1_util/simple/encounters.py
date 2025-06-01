from __future__ import annotations

from dataclasses import dataclass

from dqmj1_util.raw.btl_enmy_prm import BtlEnmyPrmEntry
from dqmj1_util.string_tables import StringTables


@dataclass
class Encounter:
    species: str
    species_id: int
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

    @staticmethod
    def from_raw(raw: BtlEnmyPrmEntry, string_tables: StringTables) -> Encounter:
        params = vars(raw)
        params = {key: value for key, value in params.items() if not key.startswith("unknown")}

        params["species"] = string_tables.species_names[raw.species_id]

        del params["skills"]
        del params["item_drops"]
        del params["skill_set_ids"]

        return Encounter(**params)
