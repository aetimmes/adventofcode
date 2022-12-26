#!/usr/bin/python3.11
"""2015 day 7."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 7
PART = "a"

LIMIT = 2**16

DATA = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    #data = lines(DATA)
    print(f"{data=}")

    circuits = {}

    q = data
    while q:
        next_ = []
        for line in q:
            ls, rs = line.split(" -> ")
            ls = ls.split()
            if len(ls) == 1:  # assignment
                if ls[0].isnumeric():
                    circuits[rs] = int(ls[0]) % LIMIT
                elif ls[0] in circuits:
                    circuits[rs] = circuits[ls[0]]
                else:
                    next_.append(line)
                continue
            if len(ls) == 2:  # not
                if ls[1] not in circuits:
                    next_.append(line)
                else:
                    circuits[rs] = ~circuits[ls[1]] % LIMIT
                continue
            if (ls[0] not in circuits and not ls[0].isnumeric()) or (
                ls[2] not in circuits and not ls[2].isnumeric()
            ):
                next_.append(line)
                continue
            if ls[1] == "AND":
                if ls[0].isnumeric():
                    circuits[rs] = circuits[ls[2]]
                else:
                    circuits[rs] = (circuits[ls[0]] & circuits[ls[2]]) % LIMIT
            elif ls[1] == "OR":
                circuits[rs] = (circuits[ls[0]] | circuits[ls[2]]) % LIMIT
            elif ls[1] == "LSHIFT":
                circuits[rs] = (circuits[ls[0]] << int(ls[2])) % LIMIT
            elif ls[1] == "RSHIFT":
                circuits[rs] = (circuits[ls[0]] >> int(ls[2])) % LIMIT
        q = next_

    result = circuits["a"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
