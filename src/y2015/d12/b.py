#!/usr/bin/python3.11
"""2015 day 12."""
import json
from aocd import get_data, submit

YEAR = 2015
DAY = 12
PART = "b"


def recursive_sum(x):
    if not x:
        return 0
    match x:
        case int():
            return x
        case list():
            return sum(recursive_sum(e) for e in x)
        case dict():
            if "red" in x.values():
                return 0
            return sum(recursive_sum(v) for k, v in x.items())
    return 0


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    j = json.loads(data)

    result = recursive_sum(j)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
