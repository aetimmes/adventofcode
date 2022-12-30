#!/usr/bin/python3.11
"""2017 day 2."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 2
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        # Generator bug:
        # nums = map(int, line.split())
        # Taking the max/min of a generator doesn't do anything.
        # Also, wrapping the generator in parentheses doesn't realize the elements, so
        # the following also doesn't work:
        # nums = (int(x) for x in line.split())
        nums = [int(x) for x in line.split()]
        result += max(nums)
        result -= min(nums)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
