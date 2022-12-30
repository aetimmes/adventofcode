#!/usr/bin/python3.11
"""2017 day 4."""
from aocd import get_data, submit
from aocd.transforms import lines
from collections import Counter

YEAR = 2017
DAY = 4
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        counters = [tuple(sorted(Counter(word).items())) for word in line.split()]
        if len(line.split()) == len(set(counters)):
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
