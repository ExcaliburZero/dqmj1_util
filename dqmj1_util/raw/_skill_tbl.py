from __future__ import annotations

from dataclasses import dataclass
from typing import IO, Literal, Optional

from dqmj1_util._region import Region

ENDIANESS: Literal["little"] = "little"


@dataclass
class SkillTblEntry:
    can_upgrade: int
    category: int
    max_skill_points: int
    unknown_a: bytes
    skill_point_requirements: list[int]
    skills: list[Skills]
    traits: list[Traits]
    species_learnt_by: list[int]
    unknown_na_and_eu_data: Optional[bytes]

    @dataclass
    class Skills:
        """
        Skills learned as a particular skill set reward.

        Has multiple skill ids if multiple skills are rewarded and/or if the skill has lower level
        skills that it replaces (ex. Frizzle replacing Frizz).
        """

        skill_ids: list[int]
        """
        Ids of the skills rewarded at the particular level of the skill set.

        Has multiple skill ids if multiple skills are rewarded and/or if the skill has lower level
        skills that it replaces (ex. Frizzle replacing Frizz).

        Always has four entries. Empty slots are represented by a skill id of 0.
        """

        unknown_a: bytes

    @dataclass
    class Traits:
        """
        Traits learned as a particular skill set reward.

        Has multiple trait ids if multiple traits are rewarded and/or if the trait has lower level
        traits that it replaces.
        """

        trait_ids: list[int]
        """
        Ids of the traits rewarded at the particular level of the skill set.

        Has multiple trait ids if multiple traits are rewarded and/or if the trait has lower level
        traits that it replaces.

        Always has four entries. Empty slots are represented by a trait id of 0.
        """

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTblEntry:
        can_upgrade = int.from_bytes(input_stream.read(1))
        category = int.from_bytes(input_stream.read(1))
        max_skill_points = int.from_bytes(input_stream.read(1))
        unknown_a = input_stream.read(1)

        skill_point_requirements = []
        for _ in range(0, 10):
            input_stream.read(2)
            skill_point_requirements.append(int.from_bytes(input_stream.read(2), ENDIANESS))

        skills = []
        for _ in range(0, 10):
            skill_ids_list = [int.from_bytes(input_stream.read(2), ENDIANESS) for _ in range(0, 4)]
            skill_unknown_a = input_stream.read(4)

            skills.append(SkillTblEntry.Skills(skill_ids=skill_ids_list, unknown_a=skill_unknown_a))

        traits = []
        for _ in range(0, 10):
            trait_id_list = [int.from_bytes(input_stream.read(1)) for _ in range(0, 4)]

            traits.append(SkillTblEntry.Traits(trait_ids=trait_id_list))

        input_stream.read(2)  # Skill set id
        input_stream.read(2)
        species_learnt_by = [int.from_bytes(input_stream.read(2), ENDIANESS) for _ in range(0, 6)]
        species_learnt_by = [i for i in species_learnt_by if i != 0]

        if region != Region.Japan:
            unknown_na_and_eu_data = input_stream.read(20)

        return SkillTblEntry(
            can_upgrade=can_upgrade,
            category=category,
            max_skill_points=max_skill_points,
            unknown_a=unknown_a,
            skill_point_requirements=skill_point_requirements,
            skills=skills,
            traits=traits,
            species_learnt_by=species_learnt_by,
            unknown_na_and_eu_data=unknown_na_and_eu_data,
        )


@dataclass
class SkillTbl:
    entries: list[SkillTblEntry]

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTbl:
        input_stream.read(8)
        entries = [SkillTblEntry.from_bin(input_stream, region) for _ in range(0, 0xC2)]

        return SkillTbl(entries)
