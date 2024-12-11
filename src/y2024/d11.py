#!/usr/bin/env python3
"""2024 day 11."""
from functools import cache
from aocd.models import Puzzle

YEAR = 2024
DAY = 11


@cache
def expand(e, n):
    if n == 0:
        return 1
    if e == 0:
        return expand(1, n-1)
    elif len(str(e)) % 2 == 0:
        temp = str(e)
        return expand(int(temp[0:len(temp)//2]), n-1) + expand(int(temp[len(temp)//2:]), n-1)
    else:
        return expand(2024*e, n-1)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        c = list(map(int, data.split()))
        for _ in range(25):
            n = []
            for e in c:
                if e == 0:
                    n.append(1)
                elif len(str(e)) % 2 == 0:
                    temp = str(e)
                    n.append(int(temp[0:len(temp)//2]))
                    n.append(int(temp[len(temp)//2:]))
                else:
                    n.append(2024 * e)
            c = n
        return len(c)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        c = list(map(int, data.split()))
        return sum(expand(e, 75) for e in c)

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
