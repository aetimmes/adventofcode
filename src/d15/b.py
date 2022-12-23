#!/usr/bin/python3.10
"""2022 day 15."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 15
PART = "b"

SCAN_BOUND = 4000000


def bounds_check(x, y):
    """Check if coords are in-bounds."""
    return 0 <= x <= SCAN_BOUND and 0 <= y <= SCAN_BOUND


def mh_dist(x1, y1, x2, y2):
    """Calculate manhattan distance between two points."""
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print("\n".join(data))

    sensors: dict[tuple[int, int], int] = {}

    for line in data:
        tokens = line.split()
        sx, sy, bx = map(int, [tokens[i][2:-1] for i in [2, 3, -2]])
        by = int(tokens[-1][2:])
        sensors[(sx, sy)] = mh_dist(sx, sy, bx, by)
        print(f"{sx=} {sy=} {bx=} {by=} {mh_dist(sx,sy,bx,by)=}")

    candidates: dict[tuple[int, int], int] = {}

    #    Consider x=5,y=5 with mhd = 2:
    # 123456789
    # 1
    # 2
    # 3    #
    # 4   ###
    # 5  ##S#B
    # 6   ###
    # 7    #
    # 8
    # 9
    #    we want to start at x +/- (mhd+1), y and iterate (mhd+1) times per side

    finalists = get_finalists(sensors, candidates)
    result = -1
    print(f"{len(finalists)=}")

    for cx, cy in finalists:
        failed = False
        for (sx, sy), mhd in sensors.items():
            if not failed and mh_dist(cx, cy, sx, sy) <= mhd:
                failed = True
                break
        if not failed:
            result = 4_000_000 * cx + cy
            break

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def get_finalists(sensors, candidates):
    """Find spots that are on the edge of 4 beacon diamonds."""
    finalists = set()
    for (sx, sy), mhd in sensors.items():
        for i in range(mhd + 2):
            d1, d2 = i, (mhd + 1 - i)

            for s1 in [1, -1]:
                for s2 in [1, -1]:
                    t = (sx + (d1 * s1), sy + (d2 * s2))
                    candidates[t] = candidates.get(t, 0) + 1
                    if candidates[t] >= 4:
                        finalists.add(t)
    return finalists


if __name__ == "__main__":
    main()
