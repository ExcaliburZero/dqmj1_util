import argparse
import json
import os
import pathlib
import sys
from dataclasses import asdict, dataclass
from typing import Any

from dqmj1_util.rom import Rom
from dqmj1_util.simple.encounter import Encounter
from dqmj1_util.simple.skill_set import SkillSet

SUCCESS = 0
FAILURE = 1


def write_guide(rom: Rom, output_directory: os.PathLike[Any] | str) -> None:
    output_directory = pathlib.Path(output_directory)
    output_directory.mkdir(exist_ok=True)

    skill_sets_directory = output_directory / "skill_sets"
    skill_sets_directory.mkdir(exist_ok=True)

    encounters = rom.load_encounters()
    skill_sets = rom.load_skill_sets()

    import jinja2 as j2

    env = j2.Environment(
        loader=j2.PackageLoader("dqmj1_util.guide"),
        autoescape=j2.select_autoescape(),
    )
    index_template = env.get_template("index.html")
    skill_sets_template = env.get_template("skill_sets.html")
    encounters_template = env.get_template("encounters.html")

    skill_set_template = env.get_template("skill_set.html")

    processed_encounters = process_encounters(encounters)
    processed_skill_sets = process_skill_sets(skill_sets)

    index_filepath = output_directory / "index.html"
    with index_filepath.open("w", encoding="utf8") as output_stream:
        output_stream.write(
            index_template.render(
                title="DQMJ1 Guide",
            )
        )

    skill_sets_filepath = output_directory / "skill_sets.html"
    with skill_sets_filepath.open("w", encoding="utf8") as output_stream:
        output_stream.write(
            skill_sets_template.render(
                title="DQMJ1 - Skill Sets",
                skill_sets=processed_skill_sets,
            )
        )

    encounters_filepath = output_directory / "encounters.html"
    with encounters_filepath.open("w", encoding="utf8") as output_stream:
        output_stream.write(
            encounters_template.render(
                title="DQMJ1 - Encounters",
                encounters=processed_encounters,
            )
        )

    for skill_set in processed_skill_sets:
        skill_set_filepath = skill_sets_directory / f"{skill_set['id']}.html"
        with skill_set_filepath.open("w", encoding="utf8") as output_stream:
            output_stream.write(
                skill_set_template.render(
                    title=f"DQMJ1 - {skill_set['name']}",
                    skill_set=skill_set,
                )
            )


def process_encounters(encounters: list[Encounter]) -> list[dict[str, Any]]:
    processed = []
    for i, encounter in enumerate(encounters):
        after = asdict(encounter)

        after["id"] = i
        after["skills"] = [
            {
                "name": encounter.skills[i],
                "id": encounter.skill_ids[i],
            }
            for i in range(0, len(encounter.skills))
        ]
        after["item_drops"] = [
            {
                "name": encounter.item_drops[i],
                "id": encounter.item_drop_item_ids[i],
            }
            for i in range(0, len(encounter.item_drops))
        ]
        after["skill_sets"] = [
            {
                "name": encounter.skill_sets[i],
                "id": encounter.skill_set_ids[i],
            }
            for i in range(0, len(encounter.skill_set_ids))
        ]

        processed.append(after)

    return processed[1:858]


def process_skill_sets(skill_sets: list[SkillSet]) -> list[dict[str, Any]]:
    processed = []
    for i, skill_set in enumerate(skill_sets):
        after = asdict(skill_set)

        after["id"] = i

        processed.append(after)

    return processed[1:-1]


@dataclass(frozen=True)
class Args:
    rom_filepath: pathlib.Path
    output_directory: pathlib.Path


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()

    parser.add_argument("--rom_filepath", required=True, type=pathlib.Path)
    parser.add_argument("--output_directory", required=True, type=pathlib.Path)

    args = Args(**vars(parser.parse_args(argv)))

    write_guide(Rom(args.rom_filepath), args.output_directory)

    return SUCCESS


def main_without_args() -> int:
    return main(sys.argv[1:])
