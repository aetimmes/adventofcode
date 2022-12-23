#!/usr/bin/python3.10
"""2022 day 3."""
from aocd import get_data, submit

YEAR = 2022
DAY = 3
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    m: dict[str, int] = {}
    for i in range(0, 26):
        m[chr(ord("a") + i)] = i + 1
        m[chr(ord("A") + i)] = i + 27

    result = 0
    current = []
    for line in data:
        current.append(line)
        if len(current) == 3:
            sets = [set(t) for t in current]
            for i in sets[0]:
                if i in sets[1] and i in sets[2]:
                    result += m[i]
                    break
            current = []
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
