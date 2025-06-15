from __future__ import annotations

from dataclasses import dataclass
from typing import IO, Annotated, Literal

import dataclasses_struct as dcs
import pandas as pd

from dqmj1_util.raw._util import BinaryReadWriteable

ENDIANESS: Literal["little"] = "little"


@dcs.dataclass_struct(size="std", byteorder="little")
class BtlEnmyPrmEntry(BinaryReadWriteable):
    """
    Encounter entry in a :class:`BtlEnmyPrm`, detailing the stats, attacks, and more of a
    particular monster.
    """

    species_id: dcs.U16
    unknown_a: Annotated[bytes, 6]
    skills: Annotated[list[EnemySkill], 6]
    item_drops: Annotated[list[ItemDrop], 2]
    gold: dcs.U16
    unknown_b: Annotated[bytes, 2]
    exp: dcs.U16
    unknown_c: Annotated[bytes, 2]
    level: dcs.U8
    unknown_d: Annotated[bytes, 1]
    unknown_e: Annotated[bytes, 1]
    scout_chance: dcs.U8
    max_hp: dcs.U16
    max_mp: dcs.U16
    attack: dcs.U16
    defense: dcs.U16
    agility: dcs.U16
    wisdom: dcs.U16
    unknown_f: Annotated[bytes, 20]
    skill_set_ids: Annotated[list[dcs.U8], 3]
    unknown_g: Annotated[bytes, 1]

    @dcs.dataclass_struct(size="std", byteorder="little")
    class ItemDrop(BinaryReadWriteable):
        item_id: dcs.U16
        chance_denominator_2_power: dcs.U16

    @dcs.dataclass_struct(size="std", byteorder="little")
    class EnemySkill(BinaryReadWriteable):
        unknown_a: Annotated[bytes, 2]
        skill_id: dcs.U16


@dataclass
class BtlEnmyPrm:
    """
    An encounter table (:code:`"BtlEnmyPrm.bin"`) listing the monsters used as battle enemies, gift
    monsters, starter monsters, etc.
    """

    entries: list[BtlEnmyPrmEntry]

    def write_bin(self, output_stream: IO[bytes]) -> None:
        magic = b"\x42\x45\x50\x54"

        output_stream.write(magic)
        output_stream.write(len(self.entries).to_bytes(4, ENDIANESS))
        for entry in self.entries:
            entry.write_bin(output_stream)

    @staticmethod
    def from_bin(input_stream: IO[bytes]) -> BtlEnmyPrm:
        input_stream.read(4)
        length = int.from_bytes(input_stream.read(4), ENDIANESS)

        entries = [BtlEnmyPrmEntry.from_bin(input_stream) for _ in range(0, length)]

        return BtlEnmyPrm(entries)

    def to_pd(self) -> pd.DataFrame:
        return pd.DataFrame(self.entries)
