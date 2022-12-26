#!/usr/bin/python3.11
"""2015 day 8."""
import re

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 8
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        newline = re.sub(r"([\\\"])", r"\\\1", line)
        print(f"{line=}, {len(line)=}, {newline=} {len(newline) + 2=}")
        result += len(newline) - len(line) + 2

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
