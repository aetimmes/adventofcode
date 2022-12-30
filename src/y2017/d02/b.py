#!/usr/bin/python3.11
"""2017 day 2."""
import itertools
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 2
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        nums = [int(x) for x in line.split()]
        # Iteration bug:
        # for (x, y) in itertools.combinations(nums, 2):
        # Combinations doesn't care about ordering, so if we encounter the combination
        # in the wrong order, we'll divide it the wrong way and skip the line.
        for (x, y) in itertools.permutations(nums, 2):
            if x % y == 0:
                result += x // y
                break

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
