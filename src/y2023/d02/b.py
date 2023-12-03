#!/usr/bin/python3.10
"""2023 day 2."""
from aocd import get_data, submit

YEAR = 2023
DAY = 2
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        line = line.split(": ")[1]
        d = {"red": 0, "green": 0, "blue": 0}
        for s in line.split("; "):
            for g in s.split(", "):
                tokens = g.split(" ")
                d[tokens[1]] = max(d[tokens[1]], int(tokens[0]))
        result += (d["red"] * d["blue"] * d["green"])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
