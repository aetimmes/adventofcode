#!/usr/bin/python3.11
"""2023 day 8b."""
from aocd import get_data, submit
import re
from math import lcm
YEAR = 2023
DAY = 8
PART = "b"

DIRECTIONS = "LR"


def main():
    """Part b."""
    chunks = get_data(day=DAY, year=YEAR).split("\n\n")

    steps = chunks[0].strip()
    m = {}
    for line in chunks[1].split("\n"):
        n, l, r = re.findall('[A-Z][A-Z][A-Z]', line, re.DOTALL)
        m[n] = [l, r]

    lengths = []
    for x in [x for x in m.keys() if x[2] == 'A']:
        i = 0
        current = x
        while current[2] != 'Z':
            current = m[current][DIRECTIONS.index(steps[i % len(steps)])]
            i += 1
        lengths.append(i)

    result = lcm(*lengths)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
