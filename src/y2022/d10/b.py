#!/usr/bin/python3.10
"""2022 day 10."""
from aocd import get_data
from aocd.transforms import lines

YEAR = 2022
DAY = 10
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = "#"  # first pixel is lit
    x = 1
    ic = 0

    pending = None

    while data:
        ic += 1
        if pending:
            x += pending
            pending = None
        else:
            line = data.pop(0)
            if line != "noop":
                pending = int(line.split()[1])
        if abs(ic % 40 - x) <= 1:
            result += "#"
        else:
            result += "."
        if ic % 40 == 39:
            result += "\n"
    print(result)


if __name__ == "__main__":
    main()
