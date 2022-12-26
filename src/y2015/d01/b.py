#!/usr/bin/python3.11
"""2015 day 1."""
from aocd import get_data, submit

YEAR = 2015
DAY = 1  # FIX ME
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    for i, c in enumerate(data):
        if c == "(":
            result += 1
        elif c == ")":
            result -= 1
        if result < 0:
            result = i+1
            break

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
