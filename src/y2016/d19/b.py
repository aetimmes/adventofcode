#!/usr/bin/python3.11
"""2016 day 19."""
from aocd import get_data, submit
from sortedcontainers import SortedSet

YEAR = 2016
DAY = 19
PART = "b"


def main():
    """Part b."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elves = SortedSet(range(1, data + 1))

    i = 0
    while len(elves) > 1:
        to_steal = (i + (len(elves)) // 2) % len(elves)
        elves.pop(to_steal)
        if i < to_steal:
            i += 1
        i %= len(elves)
    result = elves.pop()
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
