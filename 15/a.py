#!/usr/bin/python3.10
"""2022 day FIXME."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 15
PART = "a"

SCAN_LINE = 2_000_000
#SCAN_LINE = 10

DATA = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    #data = DATA.splitlines()
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
