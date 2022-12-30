#!/usr/bin/python3.11
"""2017 day 3."""
import math
from aocd import get_data, submit

YEAR = 2017
DAY = 3
PART = "b"

# r,c
deltas = ((0, 1), (-1, 0), (0, -1), (1, 0))


def nth_side_len(n):
    return math.ceil(n / 2)


def main():
    """Part b."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    (r, c) = (0, 0)
    direction = 0
    side = 1
    current_step = 1
    vals: dict[tuple[int, int], int] = {(0, 0): 1}
    while vals[(r, c)] <= data:
        r += deltas[direction][0]
        c += deltas[direction][1]
        vals[(r, c)] = sum(
            vals.get((r + dr, c + dc), 0) for dr in [-1, 0, 1] for dc in [-1, 0, 1]
        )
        print(f"{(r,c)=}, {vals[(r,c)]=}")
        current_step -= 1
        if current_step == 0:
            side += 1
            direction += 1
            direction %= 4
            current_step = nth_side_len(side)

    result = vals[(r, c)]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
