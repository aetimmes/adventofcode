#!/usr/bin/python3.10
"""2022 day 1."""
from aocd import get_data, submit

YEAR = 2022
DAY = 1
PART = "a"


def main():
    """Part a."""
    data = get_data(day=1, year=2022).split("\n")
    print(f"{data=}")

    result = 0
    current = 0
    for line in data:
        if not line:
            result = max(result, current)
            current = 0
        else:
            current += int(line)
    result = max(result, current)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
