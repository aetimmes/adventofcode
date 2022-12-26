#!/usr/bin/python3.11
"""2015 day 4."""
import hashlib

from aocd import get_data, submit

YEAR = 2015
DAY = 4  # FIX ME
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 1
    while (
        hashlib.md5((data + str(result)).encode("utf-8")).hexdigest()[0:6] != "000000"
    ):
        result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
