#!/usr/bin/python3.11
"""2022 day 25."""
import sys

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 25
PART = "a"

m = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}

rm = "=-012"


def snafutoi(a):
    """Convert a SNAFU number to an int."""
    result = 0
    for i, c in enumerate(reversed(a)):
        result += m[c] * (5**i)
    return result


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    n = 0
    for line in data:
        n += snafutoi(line)

    digits = 0
    while (5**digits) * 3 < n:
        digits += 1

    result = ""
    current = 0
    for i in range(digits, -1, -1):
        c: str = ""
        min_ = sys.maxsize
        for k, v in m.items():
            temp = abs(n - (current + (5 ** (i)) * v))
            if temp < min_:
                c = k
                min_ = temp
        result += c
        current += (5**i) * m[c]
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
