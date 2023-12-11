#!/usr/bin/python3.12
"""2023 day 11."""
from aocd.models import Puzzle
from itertools import product

YEAR = 2023
DAY = 11


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        galaxies = []
        expanded = [[], []]
        for r, line in enumerate(data.splitlines()):
            for c, ch in enumerate(line):
                if ch == "#":
                    galaxies.append([r, c])

        for i in range(len(data.splitlines())):
            for j in [0, 1]:
                if i not in (g[j] for g in galaxies):
                    print(f"expanding {'row' if j == 0 else 'column'} {i}")
                    expanded[j].append(i)

        result = 0
        for i, g1 in enumerate(galaxies):
            for j, g2 in enumerate(galaxies):
                if i >= j:
                    continue
                temp = 0
                for k in [0, 1]:
                    temp += abs(g1[k] - g2[k])
                    temp += len([x for x in expanded[k] if g1[k] < x < g2[k] or g1[k] > x > g2[k]])
                print(f"{i+1} -> {j+1}: {temp}")
                result += temp
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        galaxies = []
        expanded = [[], []]
        for r, line in enumerate(data.splitlines()):
            for c, ch in enumerate(line):
                if ch == "#":
                    galaxies.append([r, c])

        for i in range(len(data.splitlines())):
            for j in [0, 1]:
                if i not in (g[j] for g in galaxies):
                    print(f"expanding {'row' if j == 0 else 'column'} {i}")
                    expanded[j].append(i)

        result = 0
        for i, g1 in enumerate(galaxies):
            for j, g2 in enumerate(galaxies):
                if i >= j:
                    continue
                temp = 0
                for k in [0, 1]:
                    temp += abs(g1[k] - g2[k])
                    temp += 999999 * len([x for x in expanded[k] if g1[k] < x < g2[k] or g1[k] > x > g2[k]])
                print(f"{i+1} -> {j+1}: {temp}")
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
