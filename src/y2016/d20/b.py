#!/usr/bin/python3.11
"""2016 day 20."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 20
PART = "b"

MAX = 4294967295


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    ranges = [tuple(map(int, line.split("-"))) for line in data]
    ranges.append((MAX + 1, MAX + 2))
    pointer = 0
    ips = set()
    for r in sorted(ranges):
        for i in range(pointer, r[0]):
            ips.add(i)
        pointer = max(r[1] + 1, pointer)

    result = len(ips)
    print(f"{sorted(ips)=}")
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
