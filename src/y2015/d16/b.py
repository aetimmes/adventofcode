#!/usr/bin/python3.11
"""2015 day 1."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 16
PART = "b"

INPUT = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

GT = ["cats", "trees"]
LT = ["pomeranians", "goldfish"]


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    sue = {}
    for line in lines(INPUT):
        ls, rs = line.split(": ")
        sue[ls] = int(rs)

    result = -1
    for i, line in enumerate(data):
        pairs = line.split(": ", 1)[1].split(", ")
        success = True
        for p in pairs:
            ls, rs = p.split(": ")
            if ls in GT:
                if int(rs) <= sue[ls]:
                    success = False
            elif ls in LT:
                if int(rs) >= sue[ls]:
                    success = False
            elif sue.get(ls) != int(rs):
                success = False
        if success:
            result = i + 1
            break

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
