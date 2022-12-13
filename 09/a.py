#!/usr/bin/python3.10
"""2022 day 9."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 9
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    dirs = {
        "U": (1, 0),
        "D": (-1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    seen = set()

    hr, hc = 0, 0
    tr, tc = 0, 0

    for line in data:
        d, count = line.split()
        for _ in range(int(count)):
            dr, dc = dirs[d]
            hr += dr
            hc += dc
            if abs(hr - tr) == 2 or abs(hc - tc) == 2:
                if (hr - tr) > 0:
                    tr += 1
                elif (hr - tr) < 0:
                    tr -= 1
                if (hc - tc) > 0:
                    tc += 1
                elif (hc - tc) < 0:
                    tc -= 1
            seen.add((tr, tc))
    result = len(seen)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
