#!/usr/bin/python3.10
"""2022 day 3."""
from aocd import get_data, submit

YEAR = 2022
DAY = 3
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    point_map: dict[str, int] = {}
    for i in range(0, 26):
        point_map[chr(ord("a") + i)] = i + 1
        point_map[chr(ord("A") + i)] = i + 27

    result = 0
    for line in data:
        t_1 = set(line[: len(line) // 2])
        for c in line[len(line) // 2 :]:
            if c in t_1:
                result += point_map[c]
                break
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
