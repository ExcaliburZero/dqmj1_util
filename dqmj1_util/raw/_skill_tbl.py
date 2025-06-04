from __future__ import annotations

from dataclasses import dataclass
from typing import IO, Literal

from dqmj1_util._region import Region

ENDIANESS: Literal["little"] = "little"


@dataclass
class SkillTblEntry:
    can_upgrade: int
    category: int
    max_skill_points: int
    skill_point_requirements: list[int]
    skill_ids: list[list[int]]
    trait_ids: list[list[int]]
    species_learnt_by: list[int]

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTblEntry:
        can_upgrade = int.from_bytes(input_stream.read(1))
        category = int.from_bytes(input_stream.read(1))
        max_skill_points = int.from_bytes(input_stream.read(1))
        input_stream.read(1)

        skill_point_requirements = []
        for _ in range(0, 10):
            input_stream.read(2)
            skill_point_requirements.append(int.from_bytes(input_stream.read(2), ENDIANESS))

        skill_ids = []
        for _ in range(0, 10):
            skill_ids_list = [int.from_bytes(input_stream.read(2), ENDIANESS) for _ in range(0, 4)]
            skill_ids_list = [i for i in skill_ids_list if i != 0]

            input_stream.read(4)

            skill_ids.append(skill_ids_list)

        trait_ids = []
        for _ in range(0, 10):
            trait_id_list = [int.from_bytes(input_stream.read(1)) for _ in range(0, 4)]
            trait_id_list = [i for i in trait_id_list if i != 0]

            trait_ids.append(trait_id_list)

        input_stream.read(2)  # Skill set id
        input_stream.read(2)
        species_learnt_by = [int.from_bytes(input_stream.read(2), ENDIANESS) for _ in range(0, 6)]
        species_learnt_by = [i for i in species_learnt_by if i != 0]

        if region != Region.Japan:
            input_stream.read(20)

        return SkillTblEntry(
            can_upgrade=can_upgrade,
            category=category,
            max_skill_points=max_skill_points,
            skill_point_requirements=skill_point_requirements,
            skill_ids=skill_ids,
            trait_ids=trait_ids,
            species_learnt_by=species_learnt_by,
        )


@dataclass
class SkillTbl:
    entries: list[SkillTblEntry]

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTbl:
        input_stream.read(8)
        entries = [SkillTblEntry.from_bin(input_stream, region) for _ in range(0, 0xC2)]

        return SkillTbl(entries)
