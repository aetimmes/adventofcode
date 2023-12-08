#!/usr/bin/python3.11
"""2023 day 8a."""
from aocd import get_data, submit
import re
YEAR = 2023
DAY = 8
PART = "a"

DIRECTIONS = "LR"


def main():
    """Part a."""
    chunks = get_data(day=DAY, year=YEAR).split("\n\n")
    result = 0

    steps = chunks[0].strip()
    m = {}
    for line in chunks[1].split("\n"):
        n, l, r = re.findall('[A-Z][A-Z][A-Z]', line, re.DOTALL)
        m[n] = [l, r]

    current = "AAA"
    while current != "ZZZ":
        print(current)
        current = m[current][DIRECTIONS.index(steps[result % len(steps)])]
        result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
