#!/usr/bin/python3.11
"""2016 day 2."""
from aocd import get_data, submit
from aocd.transforms import lines
from numpy import array

YEAR = 2016
DAY = 2
PART = "b"

deltas = {
    "U": array([-1, 0]),
    "R": array([0, 1]),
    "D": array([1, 0]),
    "L": array([0, -1]),
}

keypad = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]


def bounds_check(r, c):
    """Check bounds."""
    return abs(r - 2) + abs(c - 2) < 3


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = ""
    position = array([1, 1])
    for line in data:
        for c in line:
            if bounds_check(*tuple(position + deltas[c])):
                position += deltas[c]
        result += str(keypad[position[0]][position[1]])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
