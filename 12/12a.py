#!/usr/bin/python3.10
"""2022 day 12."""
from aocd import get_data, submit
from aocd.transforms import lines
import sys

YEAR = 2022
DAY = 12
PART = "a"


def bounds_check(r, c, nr, nc):
    return r >= 0 and r < nr and c >= 0 and c < nc


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    start = (-1, -1)

    nr = len(data)
    nc = len(data[0])

    steps = [[sys.maxsize for _ in range(nc)] for _ in range(nr)]
    heights = [
        [ord(c) - ord("a") if c not in "SE" else 0 for c in line] for line in data
    ]
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "S":
                start = [r, c]
            if char == "E":
                end = [r, c]
    steps[start[0]][start[1]] = 0
    q = [start]
    seen = set()
    while q:
        r, c = q.pop(0)
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if bounds_check(r + dr, c + dc, nr, nc) and (r+dr, c+dc) not in seen:
                if data[r + dr][c + dc] == "E":
                    result = steps[r][c] + 1
                    print(f"{result=}")
                    submit(result, part=PART, day=DAY, year=YEAR)
                    return
                elif data[r][c] == "S" or (
                    (steps[r][c] < steps[r + dr][c + dc])
                    and (heights[r][c] - heights[r + dr][c + dc] >= -1)
                ):
                    steps[r + dr][c + dc] = steps[r][c] + 1
                    q.append([r + dr, c + dc])
                    seen.add((r+dr, c+dc))


if __name__ == "__main__":
    main()
