#!/usr/bin/python3.10
"""2022 day FIXME."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 15
PART = "a"

SCAN_LINE = 2_000_000


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print("\n".join(data))

    sensors = {}

    for line in data:
        tokens = line.split()
        sx, sy, bx = map(int, [tokens[i][2:-1] for i in [2, 3, -2]])
        by = int(tokens[-1][2:])
        sensors[(sx, sy)] = (bx, by)

    seen = set()
    for (sx, sy), (bx, by) in sensors.items():
        mh_dist = abs(bx - sx) + abs(by - sy)

        const_mh_dist = abs(sy - SCAN_LINE)

        delta_dist = abs(mh_dist - const_mh_dist)

        for i in range(delta_dist + 1):
            seen.add(sx + i)
            seen.add(sx - i)

    for (sx, sy), (bx, by) in sensors.items():
        if sy == SCAN_LINE and sx in seen:
            seen.remove(sx)
        if by == SCAN_LINE and bx in seen:
            seen.remove(bx)

    result = len(seen)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
