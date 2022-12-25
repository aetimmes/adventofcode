#!/usr/bin/python3.10
"""2022 day 20."""
import copy
from collections import deque

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 20
PART = "a"

TEST = False


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    encrypted = deque((i, int(line)) for i, line in enumerate(data))

    length = len(encrypted) - 1

    orig = list(copy.deepcopy(encrypted))

    for i, e in enumerate(orig):
        index = encrypted.index(e)
        encrypted.remove(e)
        new_index = (index + e[1]) % length
        encrypted.insert(new_index, e)

    decrypted = [e[1] for e in encrypted]
    zero_index = decrypted.index(0)
    indices = [(zero_index + i) % (len(decrypted)) for i in [1000, 2000, 3000]]
    nums = [decrypted[i] for i in indices]
    result = sum(nums)

    print(f"{result=}")
    if not TEST:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
