#!/usr/bin/python3.11
"""2016 day 22."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 22
PART = "a"

X = 0
Y = 1
USED = 2
AVAIL = 3


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    nodes = []
    for line in data[2:]:
        tokens = line.split()
        x, y = (int(t[1:]) for t in tokens[0].split("-")[1:])
        used = int(tokens[2][:-1])
        avail = int(tokens[3][:-1])
        nodes.append((x, y, used, avail))

    pairs = set()
    for node_a in nodes:
        for node_b in nodes:
            if node_a[USED] != 0 and node_a != node_b and node_a[USED] <= node_b[AVAIL]:
                pairs.add(tuple(sorted((node_a[:2], node_b[:2]))))

    result = len(pairs)
    for p in sorted(pairs):
        print(p)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
