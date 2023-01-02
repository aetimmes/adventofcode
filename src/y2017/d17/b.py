#!/usr/bin/python3.11
"""2017 day 17."""
from aocd import get_data, submit

YEAR = 2017
DAY = 17
PART = "b"


def main():
    """Part b."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    size = 1
    pos = 0
    for i in range(50_000_000):
        pos += data
        pos %= size
        if pos == 0:
            result = i + 1
        size += 1
        pos += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
