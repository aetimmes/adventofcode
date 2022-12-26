#!/usr/bin/python3.11
"""2015 day 2."""
import sys
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 2
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        tokens = [int(x) for x in line.split("x")]
        min_ = sys.maxsize
        vol = 1
        for i in range(len(tokens)):
            min_ = min(min_, 2*tokens[i] + 2*tokens[i-1])
            vol *= tokens[i]
        result += min_ + vol

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
