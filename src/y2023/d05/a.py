#!/usr/bin/python3.11
"""2023 day 5a."""
from aocd import get_data, submit
from math import floor
YEAR = 2023
DAY = 5
PART = "a"


def boundscheck(x, y, mx, my):
    return (x >= 0 and x < mx and y >= 0 and y < my)


def main():
    """Part a."""
    chunks= get_data(day=DAY, year=YEAR).split("\n\n")
    result = 99999999999999

    seeds = [int(t) for t in chunks[0].split(": ")[1].split()]
    maps = [[[int(t) for t in l.split()] for l in chunk.split("\n")[1:]] for chunk in chunks[1:]]

    from pprint import pprint
    pprint(maps)
    for seed in seeds:
        for m in maps:
            found = False
            for dst, src, rng in m:
                if (not found) and seed >= src and seed < src + rng:
                    seed = dst + (seed - src)
                    found = True
        result = min(seed, result)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
