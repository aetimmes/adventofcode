#!/usr/bin/python3.10
"""2022 day 12."""
import sys

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 12
PART = "b"


def bounds_check(r, c, nr, nc):
    """Check bounds of 2d grid."""
    return 0 <= r < nr and 0 <= c < nc


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    nr = len(data)
    nc = len(data[0])

    steps = [[sys.maxsize for _ in range(nc)] for _ in range(nr)]
    heights = [
        [ord(c) - ord("a") if c not in "SE" else 0 for c in line] for line in data
    ]
    end: tuple[int, int] = (-1, -1)
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "E":
                end = (r, c)
    steps[end[0]][end[1]] = 0
    q = [end]
    seen: set[tuple[int, int]] = set()
    seen.add(end)
    while q:
        r, c = q.pop(0)
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if bounds_check(r + dr, c + dc, nr, nc) and (r + dr, c + dc) not in seen:
                if data[r][c] == "E" or (
                    (steps[r][c] < steps[r + dr][c + dc])
                    and (heights[r][c] - heights[r + dr][c + dc] <= 1)
                ):
                    if data[r + dr][c + dc] == "a":
                        result = steps[r][c] + 1
                        print(f"{result=}")
                        submit(result, part=PART, day=DAY, year=YEAR)
                        return
                    steps[r + dr][c + dc] = steps[r][c] + 1
                    q.append((r + dr, c + dc))
                    seen.add((r + dr, c + dc))


if __name__ == "__main__":
    main()
