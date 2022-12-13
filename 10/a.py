#!/usr/bin/python3.10
"""2022 day 10."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 10
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    x = 1
    ic = 0

    pending = None

    while data:
        ic += 1
        if ic % 40 == 20:
            print(f"ic, {x*ic}")
            result += x * ic
        if pending:
            x += pending
            pending = None
        else:
            line = data.pop(0)
            if line != "noop":
                pending = int(line.split()[1])
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
