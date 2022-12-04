#!/usr/bin/python3.10
"""2022 day 2."""
from aocd import get_data, submit

YEAR = 2022
DAY = 2
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    SCORES = {"X": 1, "Y": 2, "Z": 3}

    RESULTS = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    result = 0
    for line in data:
        tokens = line.split()
        result += SCORES[tokens[1]] + RESULTS[tokens[0]][tokens[1]]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
