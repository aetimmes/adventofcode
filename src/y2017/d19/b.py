#!/usr/bin/python3.11
"""2017 day 19."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 19
PART = "b"

# r,c
dirs = ((1, 0), (0, -1), (-1, 0), (0, 1))


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    pos = (0, data[0].index("|"))
    d = 0
    while True:
        result += 1
        pos = tuple(pos[i] + dirs[d][i] for i in (0, 1))
        curr = data[pos[0]][pos[1]]
        if curr == "+":
            for delta in (-1, 1):
                (r, c) = tuple(
                    pos[i] + dirs[(d + delta) % len(dirs)][i] for i in (0, 1)
                )
                if data[r][c] != " ":
                    d += delta
                    d %= len(dirs)
                    break
        elif curr == " ":
            break
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
