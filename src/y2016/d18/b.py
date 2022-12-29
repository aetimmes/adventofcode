#!/usr/bin/python3.11
"""2016 day 18."""
from aocd import get_data, submit

YEAR = 2016
DAY = 18
PART = "b"

ROWS = 400000

U = -1
L = -1
R = 1


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    max_c = len(data)

    grid = {}
    for i, cha in enumerate(data):
        grid[(0, i)] = cha

    for r in range(1, ROWS):
        for c in range(max_c):
            if grid.get((r + U, c + L), ".") != grid.get((r + U, c + R), "."):
                grid[(r, c)] = "^"
            else:
                grid[(r, c)] = "."

    result = len([v for v in grid.values() if v == "."])
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
