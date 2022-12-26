#!/usr/bin/python3.11
"""2015 day 9."""
import itertools
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 13
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    m = defaultdict(dict)

    for line in data:
        line = line[:-1]
        t = line.split()
        val = int(t[3]) * (1 if t[2] == "gain" else -1)
        m[t[0]][t[-1]] = val

    for k in list(m.keys()):
        m[k]["Me"] = 0
        m["Me"][k] = 0

    for i in itertools.permutations(m.keys()):
        current = 0
        for j in range(len(i)):
            current += m[i[j]][i[j - 1]]
            current += m[i[j - 1]][i[j]]
        result = current if current > result else result

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
