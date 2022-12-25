#!/usr/bin/python3.10
"""2022 day 2."""
from aocd import get_data, submit

YEAR = 2022
DAY = 2
PART = "a"

SCORES = [1, 2, 3]
RESULTS = [0, 3, 6]


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        tokens = line.split()
        i_a = ord(tokens[0]) - ord("A")
        i_b = ord(tokens[1]) - ord("X")
        result += SCORES[i_b]
        result += RESULTS[(i_b - i_a + 1) % 3]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
