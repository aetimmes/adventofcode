#!/usr/bin/python3.10
"""2022 day 8."""
from aocd import get_data, submit

YEAR = 2022
DAY = 8
PART = "b"


def main():
    """Part b."""
    data = [[int(c) for c in line] for line in get_data(day=DAY, year=YEAR).split("\n")]
    print(f"{data=}")
    nr, nc = len(data), len(data[0])
    result = 0
    for r, _ in enumerate(data):
        for c, _ in enumerate(data[0]):
            score = 1
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                cr, cc = r, c
                current = 0
                while True:
                    cr += dr
                    cc += dc
                    if not bounds_check(cr, cc, nr, nc):
                        break
                    current += 1
                    if data[cr][cc] >= data[r][c]:
                        break
                score *= current
            if score > result:
                result = score
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def bounds_check(r, c, nr, nc):
    """Check bounds of 2d grid."""
    return r >= 0 and r < nr and c >= 0 and c < nc


if __name__ == "__main__":
    main()
