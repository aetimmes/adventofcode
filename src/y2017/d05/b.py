#!/usr/bin/python3.11
"""2017 day 5."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 5
PART = "b"


def main():
    """Part b."""
    data = [int(line) for line in lines(get_data(day=DAY, year=YEAR))]
    print(f"{data=}")

    result = 0
    ic = 0
    while 0 <= ic < len(data):
        result += 1
        next_ = ic + data[ic]
        if data[ic] >= 3:
            data[ic] -= 1
        else:
            data[ic] += 1
        ic = next_
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
