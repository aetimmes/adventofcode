#!/usr/bin/python3.10
"""2023 day 1."""
from aocd import get_data, submit

YEAR = 2023
DAY = 1
PART = "a"


def main():
    """Part a."""
    data = get_data(day=1, year=2023).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        first = None
        last = None
        for c in line:
            if c in '0123456789':
                if not first:
                    first = int(c)
                last = int(c)
        result += (10 * first) + last

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
