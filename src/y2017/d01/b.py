#!/usr/bin/python3.11
"""2017 day 1."""
from aocd import get_data, submit

YEAR = 2017
DAY = 1
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    length = len(data)
    for i in range(length):
        # Operator precedence bug:
        # if data[i] == data[((i + length) // 2) % length]:
        # We shouldn't be dividing i by 2 to find the element length//2 away.
        if data[i] == data[(i + (length // 2)) % length]:
            result += int(data[i])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
