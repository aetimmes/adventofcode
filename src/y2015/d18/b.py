#!/usr/bin/python3.11
"""2015 day 18."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 18
PART = "b"

STEPS = 100
DELTAS = ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    lights = {(0, 0), (0, 99), (99, 0), (99, 99)}

    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "#":
                lights.add((r, c))

    for _ in range(STEPS):
        next_ = {(0, 0), (0, 99), (99, 0), (99, 99)}
        for r in range(100):
            for c in range(100):
                neighbors = sum((r + dr, c + dc) in lights for dr, dc in DELTAS)
                if neighbors == 3 or (neighbors == 2 and (r, c) in lights):
                    next_.add((r, c))
        lights = next_

    result = len(lights)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
