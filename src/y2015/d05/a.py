#!/usr/bin/python3.11
"""2015 day 5."""
from collections import Counter

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 5  # FIX ME
PART = "a"

VOWELS = "aeiou"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        c = Counter(line)
        if sum(c[v] for v in VOWELS) < 3:
            continue
        if any(x in line for x in ["ab", "cd", "pq", "xy"]):
            continue
        for i, c in enumerate(line):
            if i < len(line) - 1 and c == line[i + 1]:
                result += 1
                break

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
