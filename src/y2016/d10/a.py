#!/usr/bin/python3.11
"""2016 day 10."""
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 10
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    inputs = defaultdict(set)
    hi_dest = {}
    lo_dest = {}

    # This definitely breaks on some inputs because I don't differentiate between bots
    # and output boxes in this version. Whoops!
    for line in sorted(data):
        tokens = line.split()
        if len(tokens) == 6:
            inputs[int(tokens[-1])].add(int(tokens[1]))
        else:
            hi_dest[int(tokens[1])] = int(tokens[-1])
            lo_dest[int(tokens[1])] = int(tokens[6])
    result = -1
    while result < 0:
        for k in hi_dest.keys():
            v = inputs[k]
            if v == {17, 61}:
                result = k
                break
            if len(v) == 2:
                inputs[lo_dest[k]].add(min(v))
                inputs[hi_dest[k]].add(max(v))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
