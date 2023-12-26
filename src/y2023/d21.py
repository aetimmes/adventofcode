#!/usr/bin/python3.12
"""2023 day 21."""
from aocd.models import Puzzle
from ..lib import DIRS4, bcg, step

YEAR = 2023
DAY = 21


def pg(locs, grid):
    print()
    for r, line in enumerate(grid):
        nl = ""
        for c, ch in enumerate(line):
            if (r, c) in locs:
                nl += "O"
            else:
                nl += ch
        print(nl)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print("\n".join(data.splitlines()))
        barriers = set()
        current = set()
        for r, line in enumerate(data.splitlines()):
            for c, ch in enumerate(line):
                if ch == "#":
                    barriers.add((r, c))
                elif ch == "S":
                    current = [(r, c)]

        for _ in range(64):
            n = set()
            while current:
                p = current.pop()
                for d in DIRS4.values():
                    np = step(p, d)
                    if bcg(*np, data) and np not in barriers:
                        n.add(np)
            current = n
            pg(current, data.splitlines())
        return len(current)

    def b(data):
        """Part b."""
        print("\n".join(data.splitlines()))

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
