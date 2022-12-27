#!/usr/bin/python3.11
"""2015 day 20."""
from aocd import get_data, submit

YEAR = 2015
DAY = 20
PART = "b"


def calc_house(n):
    """Determine how many presents house n gets."""
    result = 0
    for i in range(1, 51):
        if n % i == 0:
            result += 11 * n // i
    return result


def main():
    """Part b."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 1

    while calc_house(result) < data:
        result += 1
        if result % 10000 == 0:
            print(result, calc_house(result))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
