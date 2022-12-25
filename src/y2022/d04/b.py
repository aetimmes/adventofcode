#!/usr/bin/python3.10
"""2022 day 4."""
from aocd import get_data, submit

YEAR = 2022
DAY = 4
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        tokens = [t.split("-") for t in line.split(",")]
        le = max(int(tokens[0][0]), int(tokens[1][0]))
        ri = min(int(tokens[0][1]), int(tokens[1][1]))
        if le <= ri:
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
