#!/usr/bin/python3.10
"""2023 day 2."""
from aocd import get_data, submit

YEAR = 2023
DAY = 2
PART = "a"

DICT = {
        "red": 12,
        "green": 13,
        "blue": 14
        }


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    result = 0
    i = 0
    for line in data:
        i+=1
        valid = True
        line = line.split(": ")[1]
        for s in line.split("; "):
            if not valid:
                continue
            for g in s.split(", "):
                tokens = g.split(" ")
                if int(tokens[0]) > DICT[tokens[1]]:
                    valid = False
        if valid:
            result += i

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
