#!/usr/bin/python3.10
"""2022 day 13."""
import json

from aocd import get_data, submit

YEAR = 2022
DAY = 13
PART = "a"


def cmp(left, right):
    """Compare two elements, potentially recursively."""
    if isinstance(left, int):
        if isinstance(right, int):
            if left == right:
                return 0
            elif left < right:
                return 1
            else:
                return -1
        else:
            return cmp([left], right)
    else:
        if isinstance(right, int):
            return cmp(left, [right])
        else:
            while left and right:
                return_code = cmp(left.pop(0), right.pop(0))
                if return_code != 0:
                    return return_code
            if left:
                return -1
            if not left and not right:
                return 0
    return 1


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n\n")
    print(f"{data=}")

    result = 0
    for i, chunk in enumerate(data):
        (left, right) = [json.loads(s) for s in chunk.split("\n")]
        return_code = cmp(left, right)
        if return_code == 1:
            result += i + 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
