#!/usr/bin/python3.11
"""2017 day 9."""
from aocd import get_data, submit

YEAR = 2017
DAY = 9
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    garbage = False
    i = 0
    while i < len(data):
        c = data[i]
        if garbage:
            if c == ">":
                garbage = False
            elif c == "!":
                i += 1
            else:
                result += 1
        elif c == "<":
            garbage = True
        i += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
