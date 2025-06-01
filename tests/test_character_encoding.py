import unittest

from dqmj1_util.character_encoding import CHARACTER_ENCODINGS
from dqmj1_util.region import Region


class TestCharacterEncoding(unittest.TestCase):
    def test_string_to_bytes_empty(self) -> None:
        s = ""
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = b"\xff"
        actual = character_encoding.string_to_bytes(s)

        self.assertEqual(expected, actual)

    def test_string_to_bytes_single_character(self) -> None:
        s = "a"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = b"\x25\xff"
        actual = character_encoding.string_to_bytes(s)

        self.assertEqual(expected, actual)

    def test_string_to_bytes_multiple_characters(self) -> None:
        s = "ab"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = b"\x25\x26\xff"
        actual = character_encoding.string_to_bytes(s)

        self.assertEqual(expected, actual)

    def test_string_to_bytes_literal_character(self) -> None:
        s = "[0x99]"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = b"\x99\xff"
        actual = character_encoding.string_to_bytes(s)

        self.assertEqual(expected, actual)

    def test_string_to_bytes_escaped_character(self) -> None:
        s = "\\n"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = b"\xfe\xff"
        actual = character_encoding.string_to_bytes(s)

        self.assertEqual(expected, actual)

    def test_bytes_to_string_empty(self) -> None:
        bs = b"\xff"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = ""
        actual = character_encoding.bytes_to_string(bs)

        self.assertEqual(expected, actual)

    def test_bytes_to_string_single_character(self) -> None:
        bs = b"\x25\xff"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = "a"
        actual = character_encoding.bytes_to_string(bs)

        self.assertEqual(expected, actual)

    def test_bytes_to_string_multiple_characters(self) -> None:
        bs = b"\x25\x26\xff"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = "ab"
        actual = character_encoding.bytes_to_string(bs)

        self.assertEqual(expected, actual)

    def test_bytes_to_string_literal_character(self) -> None:
        bs = b"\xdd\xff"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = "[0xdd]"
        actual = character_encoding.bytes_to_string(bs)

        self.assertEqual(expected, actual)

    def test_bytes_to_string_escaped_character(self) -> None:
        bs = b"\xfe\xff"
        character_encoding = CHARACTER_ENCODINGS[Region.NorthAmerica]

        expected = "\\n"
        actual = character_encoding.bytes_to_string(bs)

        self.assertEqual(expected, actual)
