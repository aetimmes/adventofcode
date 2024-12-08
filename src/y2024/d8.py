#!/usr/bin/env python3
"""2024 day 8."""
from collections import defaultdict
from aocd.models import Puzzle

YEAR = 2024
DAY = 8


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        antennae = defaultdict(list)
        lines = data.splitlines()
        mr = len(lines)
        mc = len(lines[0])
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char != '.':
                    antennae[char].append((r,c,))

        antinodes = set()

        for char in antennae:
            for i, (r1,c1) in enumerate(antennae[char]):
                for (r2,c2) in antennae[char][:i] + antennae[char][i+1:]:
                    if (0 <= (2*r1-r2) < mr) and (0 <= (2*c1-c2) < mc):
                        antinodes.add((2*r1-r2,2*c1-c2,))
        print(antinodes)
        return len(antinodes)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        antennae = defaultdict(list)
        lines = data.splitlines()
        mr = len(lines)
        mc = len(lines[0])
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char != '.':
                    antennae[char].append((r,c,))

        antinodes = set()

        for char in antennae:
            for i, (r1,c1) in enumerate(antennae[char]):
                for (r2,c2) in antennae[char][:i] + antennae[char][i+1:]:
                    antinodes.add((r2,c2,))
                    dr = r1-r2
                    dc = c1-c2
                    cr, cc = r1+dr, c1+dc
                    while (0 <= cr < mr) and (0 <= cc < mc):
                        antinodes.add((cr,cc,))
                        cr += dr
                        cc += dc
        print(antinodes)
        return len(antinodes)

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
