#!/usr/bin/python3.11
"""2016 day 13."""
from collections import Counter
from aocd import get_data, submit
from numpy import array

YEAR = 2016
DAY = 13
PART = "b"


deltas = (array((1, 0)), array((0, 1)), array((-1, 0)), array((0, -1)))


def bounds_check(candidate, i: int):
    (r, c) = candidate
    return (
        r >= 0
        and c >= 0
        and Counter(str(bin(c * c + 3 * c + 2 * c * r + r + r * r + i))[2:])["1"] % 2
        == 0
    )


def main():
    """Part b."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    current = array((1, 1))
    seen = {(1, 1)}
    q = [current]
    done = False
    for _ in range(51):
        next_ = []
        while q and not done:
            current = q.pop()
            seen.add(tuple(current))
            for d in deltas:
                candidate = current + d
                if tuple(candidate) not in seen and bounds_check(candidate, data):
                    next_.append(candidate)
        q = next_

    result = len(seen)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
