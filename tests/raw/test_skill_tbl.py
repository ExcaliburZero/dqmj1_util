"""
import io
import unittest

from dqmj1_util import Region
from dqmj1_util.raw import SkillTbl, SkillTblEntry

class TestBtlEnmyPrmEntry(unittest.TestCase):
    def test_from_bin_na(self) -> None:
        region = Region.NorthAmerica

        input_stream = io.BytesIO(
            # can_upgrade
            b"\x01"
            # category
            b"\x01"
            # max_skill_points
            b"\x32"
        )

        actual = SkillTblEntry.from_bin(input_stream, region)

        expected = None
        self.assertEqual(expected, actual)
"""
