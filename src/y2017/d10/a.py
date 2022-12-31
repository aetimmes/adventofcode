#!/usr/bin/python3.11
"""2017 day 10."""
from aocd import get_data, submit

YEAR = 2017
DAY = 10
PART = "a"


def main():
    """Part a."""
    data = [int(t) for t in get_data(day=DAY, year=YEAR).split(",")]
    print(f"{data=}")

    elements = list(range(256))
    current = 0
    skip = 0
    for length in data:
        if length > len(elements):
            continue
        temp = elements + elements
        temp = (
            temp[0:current]
            + list(reversed(temp[current: current + length]))
            + temp[current + length:]
        )
        elements = (
            temp[(len(temp) // 2): len(temp) // 2 + current]
            + temp[current: len(temp) // 2]
        )
        current += length + skip
        current %= len(elements)
        skip += 1
        print(f"{elements=}")
    result = elements[0] * elements[1]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
