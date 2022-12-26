#!/usr/bin/python3.11
"""2015 day 17."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 17
PART = "b"

TARGET = 150


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    sizes_ = tuple(map(int, data))
    counts_ = tuple()
    solutions = [set() for _ in sizes_]

    def descent(target, index, sizes, counts):
        """DFS to get sums."""
        if index == len(sizes):
            if target == 0:
                solutions[sum(counts)].add(counts)
            return
        for i in [0, 1]:
            descent(target - sizes[index] * i, index + 1, sizes, counts + (i,))

    descent(TARGET, 0, sizes_, counts_)
    result = -1
    for _, s in enumerate(solutions):
        if s:
            result = len(s)
            break
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
