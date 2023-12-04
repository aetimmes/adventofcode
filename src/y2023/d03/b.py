#!/usr/bin/python3.11
"""2023 day 3b."""
from aocd import get_data, submit
from collections import defaultdict
YEAR = 2023
DAY = 3
PART = "b"


def boundscheck(x, y, mx, my):
    return (x >= 0 and x < mx and y >= 0 and y < my)


def main():
    """Part a."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    result = 0

    gears = defaultdict(set)

    for y, line in enumerate(lines):
        current = ""
        for x, c in enumerate(line):
            if c in "0123456789":
                current += c
            elif current:
                for nx in range(x-len(current)-1, x+1):
                    for ny in [y+1, y-1]:
                        if boundscheck(nx, ny, len(line), len(lines)):
                            if lines[ny][nx] == '*':
                                gears[(nx, ny)].add(int(current))

                for nx in [x, x-len(current)-1]:
                    if boundscheck(nx, y, len(line), len(lines)):
                        if lines[y][nx] == '*':
                            gears[(nx, y)].add(int(current))
                current = ""
        if current:
            x = len(line)
            for nx in range(x-len(current)-1, x+1):
                for ny in [y+1, y-1]:
                    if boundscheck(nx, ny, len(line), len(lines)):
                        if lines[ny][nx] == '*':
                            gears[(nx, ny)].add(int(current))
            for nx in [x, x-len(current)-1]:
                if boundscheck(nx, y, len(line), len(lines)):
                    if lines[y][nx] == '*':
                        gears[(nx, y)].add(int(current))
    for k in gears:
        v = list(gears[k])
        if len(v) == 2:
            result += (v[0] * v[1])
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
