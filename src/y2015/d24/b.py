#!/usr/bin/python3.11
"""2015 day 24."""
import math
import sys
from itertools import combinations

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 24
PART = "b"


def can_partition(items, target):
    """Recursively attempt to partition packages."""
    if target == 0:
        return True
    if target < 0:
        return False
    return any(can_partition(items - {item}, target - item) for item in items)


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    packages = {int(line) for line in data}

    target = sum(packages) // 4
    solution, result = None, None

    for i in range(len(data)):
        print(f"{i=}")
        result = sys.maxsize
        x = 0
        for combo in combinations(packages, i):
            x += 1
            if x % 1000 == 0:
                print(f"{x=}")
            found = False
            if sum(combo) == target:
                for j in range(len(data) - i):
                    if found:
                        break
                    for combo_2 in combinations(packages - set(combo), j):
                        if found:
                            break
                        score = math.prod(combo)
                        if sum(combo_2) == target and score < result and can_partition(
                            packages - set(combo) - set(combo_2), target
                        ):
                            result = score
                            solution = combo
                            found = True
        if result != sys.maxsize:
            break

    print(f"{target=}")
    print(f"{solution=}")
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
