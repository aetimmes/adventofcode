#!/usr/bin/python3.12
"""2023 day 14."""
from aocd.models import Puzzle

YEAR = 2023
DAY = 14


def roll(grid):
    """Roll to the north."""
    for c in range(len(grid[0])):
        anchor = 0
        for r in range(len(grid)):
            if grid[r][c] == "O":
                grid[anchor][c] = "O"
                if r != anchor:
                    grid[r][c] = "."
                anchor += 1
            if grid[r][c] == "#":
                anchor = r+1
    return grid


def roll_score(lines):
    result = 0
    for c in range(len(lines[0])):
        anchor = len(lines)
        for r in range(len(lines)):
            if lines[r][c] == "O":
                result += anchor
                anchor -= 1
            if lines[r][c] == "#":
                anchor = len(lines) - (r+1)
    return result


def score(lines):
    result = 0
    for i, line in enumerate(lines[::-1]):
        result += (i+1)*(len([x for x in line if x == "O"]))
    return result


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        lines = data.splitlines()
        return roll_score(lines)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        grid = [[c for c in line] for line in data.splitlines()]
        cache = {}
        end = 1000000000
        for i in range(1, end):
            for _ in range(4):
                grid = roll(grid)
                # NWSE so rotate 90d
                grid = list(map(list, zip(*grid[::-1])))
            tpl = tuple("".join(x) for x in grid)
            if tpl in cache:
                c_start = cache[tpl]
                c_end = i
                break
            cache[tpl] = i

        end -= c_start
        end = end % (c_end - c_start)
        end += c_start

        print(f"{c_start=}, {c_end=}")
        print(f"cycle length = {c_end - c_start}")
        print(f"{end=}")
        grid = [k for k, v in cache.items() if v == end][0]
        print(grid)
        return score(grid)

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
