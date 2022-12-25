#!/usr/bin/python3.11
"""2022 day FIXME."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = -1  # FIX ME
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
