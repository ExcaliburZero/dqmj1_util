import pathlib
import unittest

from dqmj1_util._guide import GuideData, write_guide
from tests.util import ENCOUNTERS, SKILL_SETS, SKILLS


class TestGuide(unittest.TestCase):
    def test_write_guide(self) -> None:
        """
        Only checks that it runs without crashing with an exception.
        """
        output_directory = pathlib.Path(__file__).parent / "output" / "write_guide"
        guide_data = GuideData(skills=SKILLS, skill_sets=SKILL_SETS, encounters=ENCOUNTERS)

        write_guide(guide_data, output_directory)
