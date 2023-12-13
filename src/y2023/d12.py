#!/usr/bin/python3.12
"""2023 day 12."""
from aocd.models import Puzzle
from functools import cache
import re

YEAR = 2023
DAY = 12


@cache
def resolve(springs, counts):
    if springs != springs.strip("."):
        return resolve(springs.strip("."), counts)
    if not counts:
        return 0 if "#" in springs else 1
    m = re.search(r"[\?#]+", springs)
    if not m:
        return 0
    if len(m.group()) == counts[0] and m.group()[0] == "#" and m.group()[-1] == "#":
        return resolve(springs[m.end():], counts[1:])
    elif "?" not in m.group():
        return 0
    result = 0
    for c in (".", "#"):
        result += resolve(re.sub(r"\?", c, springs, 1), counts)
    return result


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        for line in data.splitlines():
            springs, counts = line.split()
            counts = tuple(int(x) for x in counts.split(","))
            result += resolve(springs, counts)
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        for line in data.splitlines():
            springs, counts = line.split()
            counts = tuple(int(x) for x in counts.split(","))
            temp = resolve("?".join([springs]*5), counts*5)
            print(f"{springs=}, {counts=}, {temp=}")
            result += temp
        return result

    puzzle = Puzzle(year=YEAR, day=DAY)

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[part](ex.input_data)
                if (str(answer) != getattr(ex, f"answer_{part}")) and input(
                    f"Example data mismatch: {getattr(ex, f'answer_{part}')=}, {answer=}; submit anyways? [y/N]:"
                ).lower().strip() != "y":
                    exit()
            except Exception as e:
                print("Example data exception: %s" % str(e))
                if (
                    input("Example data exception; submit anyways? [y/N]:")
                    .lower()
                    .strip()
                    != "y"
                ):
                    raise
        answer = locals()[part](puzzle.input_data)
        print(f"{answer=}")
        setattr(puzzle, f"answer_{part}", answer)


if __name__ == "__main__":
    main()
