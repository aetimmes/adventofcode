#!/usr/bin/python3.11
"""2017 day 7."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 7
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    parents = {}
    nodes = set()
    for line in data:
        tokens = line.split(" -> ")
        ls = tokens[0]
        (nodename, _) = ls.split()
        nodes.add(nodename)
        if len(tokens) == 2:
            rs = tokens[1]
            for node in rs.split(", "):
                parents[node] = nodename

    roots = [node for node in nodes if node not in parents]

    result = roots[0]
    if len(roots) == 1:
        print(f"{result=}")
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
