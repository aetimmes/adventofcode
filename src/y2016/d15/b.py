#!/usr/bin/python3.11
"""2016 day 15."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 15
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    discs = [[int(line.split()[3]), int(line.split()[-1][:-1])] for line in data]
    discs.append([11, 0])
    while any(d[1] != (-i - 1) % d[0] for i, d in enumerate(discs)):
        result += 1
        for d in discs:
            d[1] += 1
            d[1] %= d[0]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
