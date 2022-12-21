#!/usr/bin/python3.10
"""2022 day 18."""
from itertools import chain
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 18
PART = "a"

deltas = list(
    chain.from_iterable(
        (
            (i, 0, 0),
            (0, i, 0),
            (0, 0, i),
        )
        for i in [1, -1]
    )
)


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elems = set()
    for line in data:
        elems.add(eval(line)) # pylint: disable=eval-used

    result = 0

    for e in elems:
        for d in deltas:
            x = tuple(e[i] + d[i] for i in range(3))
            if x not in elems:
                result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
