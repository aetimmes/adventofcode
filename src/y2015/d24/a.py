#!/usr/bin/python3.11
"""2015 day 23."""
from aocd import get_data, submit
from aocd.transforms import lines

from itertools import combinations

YEAR = 2015
DAY = 23  # FIX ME
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    packages = [int(line) for line in data]

    target = sum(packages) // 3

    for i in range(len(data)):
        min_ = -1
        for combo in combinations(packages, i):
            if sum(combo) == target:
                #do things

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
