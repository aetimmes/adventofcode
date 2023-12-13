#!/usr/bin/python3.12
"""2023 day 13."""
from aocd.models import Puzzle

YEAR = 2023
DAY = 13


def find_reflection(grid):
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            a = grid[i::-1]
            b = grid[i+1:]
            valid = True
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    valid = False
                    break
            if valid:
                return 100*(i+1)
    grid = [''.join(list(i)[::-1]) for i in zip(*grid)]
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            a = grid[i::-1]
            b = grid[i+1:]
            valid = True
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    valid = False
                    break
            if valid:
                return (i+1)


def find_smudge(grid):
    for i in range(len(grid)-1):
        a = grid[i::-1]
        b = grid[i+1:]
        diffs = 0
        for j in range(min(len(a), len(b))):
            for (m, n) in zip(a[j], b[j]):
                if m != n:
                    diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            return 100*(i+1)
    grid = [''.join(list(i)[::-1]) for i in zip(*grid)]
    for i in range(len(grid)-1):
        a = grid[i::-1]
        b = grid[i+1:]
        diffs = 0
        for j in range(min(len(a), len(b))):
            for (m, n) in zip(a[j], b[j]):
                if m != n:
                    diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            return (i+1)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        for chunk in data.split("\n\n"):
            result += find_reflection(chunk.splitlines())
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        for chunk in data.split("\n\n"):
            result += find_smudge(chunk.splitlines())
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
