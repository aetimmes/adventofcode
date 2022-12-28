#!/usr/bin/python3.11
"""2016 day 10."""
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 10
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    inputs = defaultdict(set)
    bot_hi_dest = {}
    bot_lo_dest = {}

    for line in sorted(data):
        tokens = line.split()
        if len(tokens) == 6:
            inputs[(int(tokens[-1]), "bot")].add(int(tokens[1]))
        else:
            bot_hi_dest[(int(tokens[1]), "bot")] = (int(tokens[-1]), tokens[-2])
            bot_lo_dest[(int(tokens[1]), "bot")] = (int(tokens[6]), tokens[5])

    while any(not inputs.get((i, "output")) for i in range(3)):
        keys = list(inputs.keys())
        for k in keys:
            v = inputs[k]
            if len(v) == 2:
                inputs[bot_lo_dest[k]].add(min(v))
                inputs[bot_hi_dest[k]].add(max(v))

    result = 1
    for i in range(3):
        result *= inputs[(i, "output")].pop()
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
