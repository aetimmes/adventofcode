#!/usr/bin/python3.11
"""2015 day 25."""
from aocd import get_data, submit

YEAR = 2015
DAY = 25
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    memo = {}

    tokens = data.split()
    r = int(tokens[-3][:-1])
    c = int(tokens[-1][:-1])
    code = 20151125

    result = None

    for i in range(1, r + c):
        for j in range(1, i + 1):
            if (i, j) == (r + c - 1, c):
                result = code
                break
            if code in memo:
                code = memo[code]
            else:
                initial = code
                code *= 252533
                code %= 33554393
                memo[initial] = code

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
