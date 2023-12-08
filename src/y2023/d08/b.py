#!/usr/bin/python3.11
"""2023 day 8b."""
from aocd import get_data, submit
import re
from math import lcm

YEAR = 2023
DAY = 8
PART = "b"

DIRECTIONS = {"L": 0, "R": 1}


def main():
    """Part b."""
    chunks = get_data(day=DAY, year=YEAR).split("\n\n")

    steps = chunks[0].strip()
    m = {n: [l, r] for n, l, r in (re.findall("[A-Z][A-Z][A-Z]", line, re.DOTALL) for line in chunks[1].split("\n"))}

    lengths = []
    for x in filter(lambda x: x[2] == "A", m):
        i = 0
        current = x
        while current[2] != "Z":
            current = m[current][DIRECTIONS[(steps[i % len(steps)])]]
            i += 1
        lengths.append(i)

    result = lcm(*lengths)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
