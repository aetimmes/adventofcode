#!/usr/bin/python3.11
"""2017 day 13."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 13
PART = "a"


def main():
    """Part a."""
    ranges, dirs, positions = parse_input()

    result = 0
    for t in range(max(ranges.keys()) + 1):
        if positions.get(t, -1) == 0:
            result += t * ranges[t]
        for k, v in ranges.items():
            positions[k] += dirs[k]
            if positions[k] in {0, v - 1}:
                dirs[k] *= -1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def parse_input():
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")
    ranges = {}
    for line in data:
        ls, rs = (int(t) for t in line.split(": "))
        ranges[ls] = rs
    dirs = {r: 1 for r in ranges}
    positions = {r: 0 for r in ranges}
    return ranges, dirs, positions


if __name__ == "__main__":
    main()
