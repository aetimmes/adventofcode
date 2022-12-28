#!/usr/bin/python3.11
"""2016 day 3."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 3
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        sides = sorted((int(x) for x in line.split()))
        if sides[0] + sides[1] > sides[2]:
            result += 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
