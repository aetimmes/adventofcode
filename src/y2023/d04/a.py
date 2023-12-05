#!/usr/bin/python3.11
"""2023 day 4a."""
from aocd import get_data, submit
from math import floor
YEAR = 2023
DAY = 4
PART = "a"


def boundscheck(x, y, mx, my):
    return (x >= 0 and x < mx and y >= 0 and y < my)


def main():
    """Part a."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    result = 0
    for line in lines:
        halves = line.split(": ")[1].split(" | ")
        l = [int(i) for i in halves[0].split()]
        r = [int(i) for i in halves[1].split()]
        matches = sum([1 for i in l if i in r])-1
        result += floor(2 ** matches)


    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
