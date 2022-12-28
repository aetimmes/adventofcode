#!/usr/bin/python3.11
"""2016 day 3."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 3
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    triangles = [[], [], []]
    for i, line in enumerate(data):
        for j, t in enumerate(line.split()):
            triangles[j].append(int(t))
        if i % 3 == 2:
            for t in triangles:
                sides = sorted((int(x) for x in t))
                if sides[0] + sides[1] > sides[2]:
                    result += 1
            triangles = [[], [], []]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
