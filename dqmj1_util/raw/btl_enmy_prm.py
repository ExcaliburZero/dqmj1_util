from dataclasses import dataclass
from typing import IO, Literal

import pandas as pd

ENDIANESS: Literal["little"] = "little"


@dataclass
class ItemDrop:
    item_id: int
    chance_denominator_2_power: int

    def write_bin(self, output_stream: IO[bytes]) -> None:
        output_stream.write(self.item_id.to_bytes(2, ENDIANESS))
        output_stream.write(self.chance_denominator_2_power.to_bytes(2, ENDIANESS))

    @staticmethod
    def from_bin(input_stream: IO[bytes]) -> "ItemDrop":
        item_id = int.from_bytes(input_stream.read(2), ENDIANESS)
        chance_denominator_2_power = int.from_bytes(input_stream.read(2), ENDIANESS)

        return ItemDrop(item_id=item_id, chance_denominator_2_power=chance_denominator_2_power)


@dataclass
class EnemySkillEntry:
    unknown_a: int
    skill_id: int

    def write_bin(self, output_stream: IO[bytes]) -> None:
        output_stream.write(self.unknown_a.to_bytes(2, ENDIANESS))
        output_stream.write(self.skill_id.to_bytes(2, ENDIANESS))

    @staticmethod
    def from_bin(input_stream: IO[bytes]) -> "EnemySkillEntry":
        unknown_a = int.from_bytes(input_stream.read(2), ENDIANESS)
        skill_id = int.from_bytes(input_stream.read(2), ENDIANESS)

        return EnemySkillEntry(unknown_a=unknown_a, skill_id=skill_id)


@dataclass
class BtlEnmyPrmEntry:
    """
    Encounter entry in a :class:`BtlEnmyPrm`, detailing the stats, attacks, and more of a
    particular monster.
    """

    species_id: int
    unknown_a: bytes
    skills: list[EnemySkillEntry]
    item_drops: list[ItemDrop]
    gold: int
    unknown_b: bytes
    exp: int
    unknown_c: bytes
    level: int
    unknown_d: int
    unknown_e: int
    scout_chance: int
    max_hp: int
    max_mp: int
    attack: int
    defense: int
    agility: int
    wisdom: int
    unknown_f: bytes
    skill_set_ids: list[int]
    unknown_g: bytes

    def write_bin(self, output_stream: IO[bytes]) -> None:
        output_stream.write(self.species_id.to_bytes(2, ENDIANESS))
        output_stream.write(self.unknown_a)
        for skill in self.skills:
            skill.write_bin(output_stream)
        for item_drop in self.item_drops:
            item_drop.write_bin(output_stream)
        output_stream.write(self.gold.to_bytes(2, ENDIANESS))
        output_stream.write(self.unknown_b)
        output_stream.write(self.exp.to_bytes(2, ENDIANESS))
        output_stream.write(self.unknown_c)
        output_stream.write(self.level.to_bytes(1, ENDIANESS))
        output_stream.write(self.unknown_d.to_bytes(1, ENDIANESS))
        output_stream.write(self.unknown_e.to_bytes(1, ENDIANESS))
        output_stream.write(self.scout_chance.to_bytes(1, ENDIANESS))
        output_stream.write(self.max_hp.to_bytes(2, ENDIANESS))
        output_stream.write(self.max_mp.to_bytes(2, ENDIANESS))
        output_stream.write(self.attack.to_bytes(2, ENDIANESS))
        output_stream.write(self.defense.to_bytes(2, ENDIANESS))
        output_stream.write(self.agility.to_bytes(2, ENDIANESS))
        output_stream.write(self.wisdom.to_bytes(2, ENDIANESS))
        output_stream.write(self.unknown_f)
        for skill_set_id in self.skill_set_ids:
            output_stream.write(skill_set_id.to_bytes(1, ENDIANESS))
        output_stream.write(self.unknown_g)

    @staticmethod
    def from_bin(input_stream: IO[bytes]) -> "BtlEnmyPrmEntry":
        species_id = int.from_bytes(input_stream.read(2), ENDIANESS)

        unknown_a = input_stream.read(6)
        skills = [EnemySkillEntry.from_bin(input_stream) for _ in range(0, 6)]
        item_drops = [ItemDrop.from_bin(input_stream) for _ in range(0, 2)]
        gold = int.from_bytes(input_stream.read(2), ENDIANESS)
        unknown_b = input_stream.read(2)
        exp = int.from_bytes(input_stream.read(2), ENDIANESS)
        unknown_c = input_stream.read(2)
        level = int.from_bytes(input_stream.read(1), ENDIANESS)
        unknown_d = int.from_bytes(input_stream.read(1), ENDIANESS)

        unknown_e = int.from_bytes(input_stream.read(1), ENDIANESS)
        scout_chance = int.from_bytes(input_stream.read(1), ENDIANESS)
        max_hp = int.from_bytes(input_stream.read(2), ENDIANESS)
        max_mp = int.from_bytes(input_stream.read(2), ENDIANESS)
        attack = int.from_bytes(input_stream.read(2), ENDIANESS)
        defense = int.from_bytes(input_stream.read(2), ENDIANESS)
        agility = int.from_bytes(input_stream.read(2), ENDIANESS)
        wisdom = int.from_bytes(input_stream.read(2), ENDIANESS)

        unknown_f = input_stream.read(20)
        skill_set_ids = [int.from_bytes(input_stream.read(1)) for _ in range(0, 3)]

        unknown_g = input_stream.read(1)

        return BtlEnmyPrmEntry(
            species_id=species_id,
            unknown_a=unknown_a,
            skills=skills,
            item_drops=item_drops,
            gold=gold,
            unknown_b=unknown_b,
            exp=exp,
            unknown_c=unknown_c,
            level=level,
            unknown_d=unknown_d,
            unknown_e=unknown_e,
            scout_chance=scout_chance,
            max_hp=max_hp,
            max_mp=max_mp,
            attack=attack,
            defense=defense,
            agility=agility,
            wisdom=wisdom,
            unknown_f=unknown_f,
            skill_set_ids=skill_set_ids,
            unknown_g=unknown_g,
        )


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
    def from_bin(input_stream: IO[bytes]) -> "BtlEnmyPrm":
        input_stream.read(4)
        length = int.from_bytes(input_stream.read(4), ENDIANESS)

        entries = [BtlEnmyPrmEntry.from_bin(input_stream) for _ in range(0, length)]

        return BtlEnmyPrm(entries)

    def to_pd(self) -> pd.DataFrame:
        return pd.DataFrame(self.entries)
