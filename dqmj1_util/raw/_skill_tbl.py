from __future__ import annotations

from dataclasses import dataclass
from typing import IO, Annotated, Literal, cast

import dataclasses_struct as dcs

from dqmj1_util._region import Region
from dqmj1_util.raw._util import BinaryReadWriteable

ENDIANESS: Literal["little"] = "little"


class SkillTblEntryBase:
    can_upgrade: dcs.U8
    category: dcs.U8
    max_skill_points: dcs.U8
    unknown_a: Annotated[bytes, 1]
    skill_point_requirements: Annotated[list[SkillTblEntry.SkillPointRequirement], 10]
    skills: Annotated[list[SkillTblEntry.Skills], 10]
    traits: Annotated[list[SkillTblEntry.Traits], 10]
    skill_set_id: dcs.U16
    unknown_b: Annotated[bytes, 2]
    species_learnt_by: Annotated[list[dcs.U16], 6]

    @property
    def num_rewards(self) -> int:
        prev_point_total = 0
        for i, requirement in enumerate(self.skill_point_requirements):
            if requirement.points_total == prev_point_total:
                return i

            prev_point_total = requirement.points_total

        return len(self.skill_point_requirements)


class SkillTblEntry:
    @dcs.dataclass_struct(size="std", byteorder="little")
    class SkillPointRequirement:
        points_delta: dcs.U16
        points_total: dcs.U16

    @dcs.dataclass_struct(size="std", byteorder="little")
    class Skills:
        """
        Skills learned as a particular skill set reward.

        Has multiple skill ids if multiple skills are rewarded and/or if the skill has lower level
        skills that it replaces (ex. Frizzle replacing Frizz).
        """

        skill_ids: Annotated[list[dcs.U16], 4]
        """
        Ids of the skills rewarded at the particular level of the skill set.

        Has multiple skill ids if multiple skills are rewarded and/or if the skill has lower level
        skills that it replaces (ex. Frizzle replacing Frizz).

        Always has four entries. Empty slots are represented by a skill id of 0.
        """

        unknown_a: Annotated[bytes, 4]

        def __len__(self) -> int:
            return sum(1 for skill_id in self.skill_ids if skill_id != 0)

    @dcs.dataclass_struct(size="std", byteorder="little")
    class Traits:
        """
        Traits learned as a particular skill set reward.

        Has multiple trait ids if multiple traits are rewarded and/or if the trait has lower level
        traits that it replaces.
        """

        trait_ids: Annotated[list[dcs.U8], 4]
        """
        Ids of the traits rewarded at the particular level of the skill set.

        Has multiple trait ids if multiple traits are rewarded and/or if the trait has lower level
        traits that it replaces.

        Always has four entries. Empty slots are represented by a trait id of 0.
        """

        def __len__(self) -> int:
            return sum(1 for trait_id in self.trait_ids if trait_id != 0)

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTblEntryJp | SkillTblEntryNaEu:
        if region == Region.Japan:
            return SkillTblEntryJp.from_bin(input_stream)
        else:
            return SkillTblEntryNaEu.from_bin(input_stream)


@dcs.dataclass_struct(size="std", byteorder="little")
class SkillTblEntryJp(SkillTblEntryBase, BinaryReadWriteable):
    can_upgrade: dcs.U8
    category: dcs.U8
    max_skill_points: dcs.U8
    unknown_a: Annotated[bytes, 1]
    skill_point_requirements: Annotated[list[SkillTblEntry.SkillPointRequirement], 10]
    skills: Annotated[list[SkillTblEntry.Skills], 10]
    traits: Annotated[list[SkillTblEntry.Traits], 10]
    skill_set_id: dcs.U16
    unknown_b: Annotated[bytes, 2]
    species_learnt_by: Annotated[list[dcs.U16], 6]


@dcs.dataclass_struct(size="std", byteorder="little")
class SkillTblEntryNaEu(SkillTblEntryBase, BinaryReadWriteable):
    can_upgrade: dcs.U8
    category: dcs.U8
    max_skill_points: dcs.U8
    unknown_a: Annotated[bytes, 1]
    skill_point_requirements: Annotated[list[SkillTblEntry.SkillPointRequirement], 10]
    skills: Annotated[list[SkillTblEntry.Skills], 10]
    traits: Annotated[list[SkillTblEntry.Traits], 10]
    skill_set_id: dcs.U16
    unknown_b: Annotated[bytes, 2]
    species_learnt_by: Annotated[list[dcs.U16], 6]
    unknown_c: Annotated[bytes, 20]


@dataclass
class SkillTbl:
    entries: list[SkillTblEntryJp] | list[SkillTblEntryNaEu]

    def write_bin(self, output_stream: IO[bytes]) -> None:
        magic = b"\x53\x4b\x49\x4c"

        output_stream.write(magic)
        output_stream.write(len(self.entries).to_bytes(4, ENDIANESS))
        for entry in self.entries:
            entry.write_bin(output_stream)

    @staticmethod
    def from_bin(input_stream: IO[bytes], region: Region) -> SkillTbl:
        input_stream.read(4)
        length = int.from_bytes(input_stream.read(4), ENDIANESS)

        entries = cast(
            "list[SkillTblEntryJp] | list[SkillTblEntryNaEu]",
            [SkillTblEntry.from_bin(input_stream, region) for _ in range(0, length)],
        )

        return SkillTbl(entries)
