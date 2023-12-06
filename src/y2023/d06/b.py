#!/usr/bin/python3.11
"""2023 day 6b."""
from aocd import get_data, submit
from math import floor
YEAR = 2023
DAY = 6
PART = "b"


def main():
    """Part b."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    result = 0
    t = int("".join(lines[0].split(": ")[1].split()))
    d = int("".join(lines[1].split(": ")[1].split()))

    start = t//2
    for i in range(start, t):
        if i * (t - i) > d:
            result += 1
        else:
            break
    result *= 2
    if t % 2 == 0:
        result -= 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
