#!/usr/bin/python3.11
"""2017 day 20."""
import sys
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 20
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    positions = []
    velocities = []
    accelerations = []
    for line in data:
        p, v, a = line.split(", ")
        positions.append(list(map(int, p[3:-1].split(","))))
        velocities.append(list(map(int, v[3:-1].split(","))))
        accelerations.append(list(map(int, a[3:-1].split(","))))
    result = -1
    min_ = sys.maxsize
    for i, accels in enumerate(accelerations):
        curr = sum(abs(a) for a in accels)
        if curr < min_:
            result = i
            min_ = curr

    print(f"{result=}")
    if result >= 0:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
