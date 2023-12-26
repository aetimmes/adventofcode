#!/usr/bin/python3.12
"""2023 day 23."""
from copy import deepcopy
from aocd.models import Puzzle
from ..lib import DIRS4, step

YEAR = 2023
DAY = 23

SLOPES = {">": "E", "V": "S", "v": "S", "<": "W", "^": "N"}


def pg(grid, seen):
    """print grid"""
    print()
    for r, line in enumerate(grid):
        l = ""
        for c, ch in enumerate(line):
            if (r, c) in seen:
                l += "O"
            else:
                l += ch
        print(l)


def main():
    """Main."""

    def a(data):
        """Part a."""
        lines = data.splitlines()
        print("\n".join(lines))
        result = 0
        locs: dict[tuple[int, int], str] = {}
        for r, line in enumerate(lines):
            for c, ch in enumerate(line):
                if ch != "#":
                    locs[(r, c)] = ch
        stack: list[tuple[set[tuple[int, int]], tuple[int, int]]] = [(set(), (0, 1))]
        while stack:
            seen, pos = stack.pop()
            seen.add(pos)
            if (pos == (len(lines)-1, len(lines[0]) - 2)) and (len(seen) > result):
                result = len(seen)-1
                print(f"new max: {result}")
                continue

            if isinstance(locs.get(pos), str) and locs.get(pos) in ">vV<^":
                ns = [DIRS4[SLOPES[locs[pos]]]]
            elif locs.get(pos) == ".":
                ns = list(DIRS4.values())
            else:
                ns = []
            for s in ns:
                nl = step(pos, s)
                if locs.get(nl) and nl not in seen:
                    stack.append((seen.copy(), nl))
        return result

    def b(data):
        """Part b."""
        lines = data.splitlines()
        print("\n".join(lines))
        result = 0
        locs: dict[tuple[int, int], str] = {}
        for r, line in enumerate(lines):
            for c, ch in enumerate(line):
                if ch != "#":
                    locs[(r, c)] = ch
        stack: list[tuple[set[tuple[int, int]], tuple[int, int]]] = [(set(), (0, 1))]
        while stack:
            seen, pos = stack.pop()
            seen.add(pos)
            if (pos == (len(lines)-1, len(lines[0]) - 2)) and (len(seen) > result):
                result = len(seen)-1
                print(f"new max: {result}")
                continue

            ns = list(DIRS4.values())
            for s in ns:
                nl = step(pos, s)
                if locs.get(nl) and nl not in seen:
                    stack.append((seen.copy(), nl))
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
