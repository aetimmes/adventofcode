#!/usr/bin/env python3
"""2024 day 1."""
from aocd.models import Puzzle
from collections import Counter

YEAR = 2024
DAY = 1


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        l, r = [], []
        for line in data.splitlines():
            line = list(map(int, line.split()))
            l.append(line[0])
            r.append(line[1])
        l = sorted(l)
        r = sorted(r)
        result = 0
        for i in range(len(l)):
            result += abs(l[i] - r[i])
        return result
            

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        l, r = [], []
        for line in data.splitlines():
            line = list(map(int, line.split()))
            l.append(line[0])
            r.append(line[1])

        c = Counter(r)
        result = 0
        for i in l:
            result += i * c[i]
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
