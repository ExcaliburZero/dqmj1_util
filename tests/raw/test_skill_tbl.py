import io
import unittest

from dqmj1_util import Region
from dqmj1_util.raw import SkillTblEntry, SkillTblEntryJp, SkillTblEntryNaEu


class TestBtlEnmyPrmEntry(unittest.TestCase):
    def test_from_bin_na(self) -> None:
        region = Region.NorthAmerica
        input_stream = io.BytesIO(
            # can_upgrade
            b"\x01"
            # category
            b"\x02"
            # max_skill_points
            b"\x32"
            # unknown_a
            b"\x00"
            # skill_point_requirements
            b"\x03\x00\x03\x00"
            b"\x03\x00\x06\x00"
            b"\x03\x00\x09\x00"
            b"\x03\x00\x0c\x00"
            b"\x03\x00\x0f\x00"
            b"\x03\x00\x12\x00"
            b"\x03\x00\x15\x00"
            b"\x03\x00\x18\x00"
            b"\x03\x00\x1b\x00"
            b"\x03\x00\x1e\x00"
            # skills
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x02\x00\x03\x00\x04\x00\x05\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            # traits
            b"\x04\x05\x06\x07"
            b"\x02\x03\x04\x05"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            # skill_set_id
            b"\x02\x00"
            # unknown_b
            b"\x01\x02"
            # species_learnt_by
            b"\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            # unknown_c
            b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )
        actual = SkillTblEntry.from_bin(input_stream, region)
        expected = SkillTblEntryNaEu(
            can_upgrade=1,
            category=2,
            max_skill_points=50,
            unknown_a=b"\x00",
            skill_point_requirements=[
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=3),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=6),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=9),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=12),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=15),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=18),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=21),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=24),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=27),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=30),
            ],
            skills=[
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[2, 3, 4, 5], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
            ],
            traits=[
                SkillTblEntry.Traits(trait_ids=[4, 5, 6, 7]),
                SkillTblEntry.Traits(trait_ids=[2, 3, 4, 5]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
            ],
            skill_set_id=2,
            unknown_b=b"\x01\x02",
            species_learnt_by=[1, 2, 0, 0, 0, 0],
            unknown_c=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        )
        self.assertEqual(expected, actual)

    def test_from_bin_jp(self) -> None:
        region = Region.Japan
        input_stream = io.BytesIO(
            # can_upgrade
            b"\x01"
            # category
            b"\x02"
            # max_skill_points
            b"\x32"
            # unknown_a
            b"\x00"
            # skill_point_requirements
            b"\x03\x00\x03\x00"
            b"\x03\x00\x06\x00"
            b"\x03\x00\x09\x00"
            b"\x03\x00\x0c\x00"
            b"\x03\x00\x0f\x00"
            b"\x03\x00\x12\x00"
            b"\x03\x00\x15\x00"
            b"\x03\x00\x18\x00"
            b"\x03\x00\x1b\x00"
            b"\x03\x00\x1e\x00"
            # skills
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x02\x00\x03\x00\x04\x00\x05\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            b"\x01\x00\x02\x00\x03\x00\x04\x00\x00\x00\x00\x00"
            # traits
            b"\x04\x05\x06\x07"
            b"\x02\x03\x04\x05"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            b"\x01\x02\x03\x04"
            # skill_set_id
            b"\x02\x00"
            # unknown_b
            b"\x01\x02"
            # species_learnt_by
            b"\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )
        actual = SkillTblEntry.from_bin(input_stream, region)
        expected = SkillTblEntryJp(
            can_upgrade=1,
            category=2,
            max_skill_points=50,
            unknown_a=b"\x00",
            skill_point_requirements=[
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=3),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=6),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=9),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=12),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=15),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=18),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=21),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=24),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=27),
                SkillTblEntry.SkillPointRequirement(points_delta=3, points_total=30),
            ],
            skills=[
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[2, 3, 4, 5], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
                SkillTblEntry.Skills(skill_ids=[1, 2, 3, 4], unknown_a=b"\x00\x00\x00\x00"),
            ],
            traits=[
                SkillTblEntry.Traits(trait_ids=[4, 5, 6, 7]),
                SkillTblEntry.Traits(trait_ids=[2, 3, 4, 5]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
                SkillTblEntry.Traits(trait_ids=[1, 2, 3, 4]),
            ],
            skill_set_id=2,
            unknown_b=b"\x01\x02",
            species_learnt_by=[1, 2, 0, 0, 0, 0],
        )
        self.assertEqual(expected, actual)
