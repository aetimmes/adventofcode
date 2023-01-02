#!/usr/bin/python3.11
"""2017 day 12."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 12
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    connections = {}

    for line in data:
        ls, rs = line.split(" <-> ")
        connections[ls] = rs.split(", ")
    programs = set(connections.keys())
    result = 0
    while programs:
        result += 1
        q = [programs.pop()]
        while q:
            current = q.pop()
            programs.discard(current)
            q.extend([c for c in connections[current] if c in programs])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
