#!/usr/bin/python3.11
"""2023 day 6a."""
from aocd import get_data, submit
from math import floor
YEAR = 2023
DAY = 6
PART = "a"


def main():
    """Part a."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    result = 1
    times = map(int, lines[0].split(": ")[1].split())
    distances = map(int, lines[1].split(": ")[1].split())

    for t, d in zip(times, distances):
        current = 0
        for i in range(t):
            if i*(t-i) > d:
                current+=1
        result *= current
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
