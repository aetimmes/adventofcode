#!/usr/bin/python3.10
"""2023 day 1."""
from aocd import get_data, submit

YEAR = 2023
DAY = 1
PART = "b"

m = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        }

LOL = 9999999999999


def main():
    """Part b."""
    data = get_data(day=1, year=2023).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        mins = [LOL] * 10
        maxs = [-1] * 10
        for i in range(10):
            try:
                mins[i] = line.index(str(i))
            except Exception:
                mins[i] = LOL
            try:
                mins[i] = min(mins[i], line.index(m[i]))
            except Exception:
                pass
            try:
                maxs[i] = line.rindex(str(i))
            except Exception:
                maxs[i] = -1
            try:
                maxs[i] = max(maxs[i], line.rindex(m[i]))
            except Exception:
                pass
        result += 10 * mins.index(min(mins))
        result += maxs.index(max(maxs))
    print(result)
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
