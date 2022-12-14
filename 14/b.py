#!/usr/bin/python3.10
"""2022 day 14."""
import sys

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 14
PART = "b"


def draw_line(sr, sc, er, ec, grid):
    """Add a line of sand."""
    if sr != er:
        sign = (er > sr) - (er < sr)
        for ir in range(sr, er + sign, sign):
            grid[ir][sc] = "#"
    else:
        sign = (ec > sc) - (ec < sc)
        for ic in range(sc, ec + sign, sign):
            grid[sr][ic] = "#"
    return grid


def print_graph(grid, min_c, max_c, abyss_level):
    """Print the graph."""
    result = ""
    for r in range(0, abyss_level + 6):
        result += "".join(grid[r][min_c - 10 : max_c + 10]) + "\n"
    return result


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    grid = [["." for _ in range(1000)] for _ in range(1000)]

    abyss_level = 0

    min_c = sys.maxsize
    max_c = 0

    for line in data:
        cr, cc = None, None
        tokens = line.split(" -> ")
        for token in tokens:
            if not cr:
                (cc, cr) = map(int, token.split(","))
            else:
                (nc, nr) = map(int, token.split(","))
                grid = draw_line(cr, cc, nr, nc, grid)
                cr, cc = nr, nc
            abyss_level = max(cr + 2, abyss_level)
            if cc < min_c:
                min_c = cc
            if max_c < cc:
                max_c = cc

    grid[abyss_level] = ["#" for _ in grid[abyss_level]]

    result = 0
    for i in range(sys.maxsize):
        cr, cc = 0, 500
        while True:
            if grid[0][500] == "x":
                break
            elif grid[cr + 1][cc] == ".":
                cr += 1
            elif grid[cr + 1][cc - 1] == ".":
                cr += 1
                cc -= 1
            elif grid[cr + 1][cc + 1] == ".":
                cr += 1
                cc += 1
            else:
                grid[cr][cc] = "x"
                break
        if grid[0][500] == "x":
            result = i + 1
            break

    print(print_graph(grid, min_c, max_c, abyss_level))
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
