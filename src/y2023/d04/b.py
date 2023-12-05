#!/usr/bin/python3.11
"""2023 day 4b."""
from aocd import get_data, submit
YEAR = 2023
DAY = 4
PART = "b"


def boundscheck(x, y, mx, my):
    return (x >= 0 and x < mx and y >= 0 and y < my)


def main():
    """Part b."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    cards = [1] * len(lines)
    for n, line in enumerate(lines):
        halves = line.split(": ")[1].split(" | ")
        l = [int(i) for i in halves[0].split()]
        r = [int(i) for i in halves[1].split()]
        matches = sum([1 for i in l if i in r])-1
        for d in range(n+1, n+matches+2):
            cards[d] += cards[n]

    result = sum(cards)
    print(f"{cards=}")
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
