#!/usr/bin/python3.11
"""2016 day 1."""
from aocd import get_data, submit
from numpy import array

YEAR = 2016
DAY = 1
PART = "b"

deltas = [array([-1, 0]), array([0, 1]), array([1, 0]), array([0, -1])]

turns = {"L": -1, "R": 1}


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split(", ")
    print(f"{data=}")

    position = array([0, 0])
    facing = 0

    seen = {(0, 0)}

    found = False
    for token in data:
        facing += turns[token[0]]
        facing %= 4
        for _ in range(int(token[1:])):
            position += deltas[facing]
            if tuple(position) in seen:
                print(f"{position=}")
                found = True
                break
            seen.add(tuple(position))
        if found:
            break

    result = sum(abs(position))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
