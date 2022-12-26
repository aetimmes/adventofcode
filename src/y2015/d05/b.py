#!/usr/bin/python3.11
"""2015 day 5."""
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 5  # FIX ME
PART = "b"

VOWELS = "aeiou"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    for line in data:
        a, b = False, False
        seen = defaultdict(list)
        for i in range(len(line) - 1):
            if seen[line[i : i + 2]] and (
                len(seen[line[i : i + 2]]) > 1 or seen[line[i : i + 2]][0] != i - 1
            ):
                a = True
                print(
                    f"found {line[i:i+2]} twice in {line} at positions {i} and {seen[line[i:i+2]]}"
                )
                break
            seen[line[i : i + 2]].append(i)
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                b = True
                break
        if a and b:
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
