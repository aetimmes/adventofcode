#!/usr/bin/python3.10
"""2022 day 8."""
from aocd import get_data, submit

YEAR = 2022
DAY = 8
PART = "a"


def main():
    """Part a."""
    data = [[int(c) for c in line] for line in get_data(day=DAY, year=YEAR).split("\n")]
    print(f"{data=}")

    visible: set[tuple[int, int]] = set()
    for r, row in enumerate(data):
        for direction in [1, -1]:
            current = None
            for c, digit in list(enumerate(row))[::direction]:
                if (current is None) or (digit > current):
                    current = digit
                    visible.add(
                        (
                            r,
                            c,
                        )
                    )

    for c in range(len(data)):
        for direction in [1, -1]:
            current = None
            for r, digit in list(enumerate([row[c] for row in data]))[::direction]:
                if (current is None) or (digit > current):
                    current = digit
                    visible.add(
                        (
                            r,
                            c,
                        )
                    )

    result = len(visible)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
