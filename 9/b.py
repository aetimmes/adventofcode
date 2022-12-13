#!/usr/bin/python3.10
"""2022 day 9."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 9
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    dirs = {
        "U": (1, 0),
        "D": (-1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    seen = set()

    knots = [[0, 0] for _ in range(10)]

    for line in data:
        d, count = line.split()
        for _ in range(int(count)):
            dr, dc = dirs[d]
            knots[0][0] += dr
            knots[0][1] += dc
            for i in range(1, 10):
                knots[i] = helper(knots[i - 1], knots[i])
            seen.add((knots[-1][0], knots[-1][1]))
    result = len(seen)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def helper(head, tail):
    hr, hc = head
    tr, tc = tail
    if abs(hr - tr) == 2 or abs(hc - tc) == 2:
        if (hr - tr) > 0:
            tr += 1
        elif (hr - tr) < 0:
            tr -= 1
        if (hc - tc) > 0:
            tc += 1
        elif (hc - tc) < 0:
            tc -= 1
    return [tr, tc]


if __name__ == "__main__":
    main()
