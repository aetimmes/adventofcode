#!/usr/bin/python3.11
"""2015 day 9."""
from collections import defaultdict
import itertools
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 9  # FIX ME
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    m = defaultdict(dict)

    for line in data:
        t = line.split()
        m[t[0]][t[2]] = int(t[-1])
        m[t[2]][t[0]] = int(t[-1])

    for i in itertools.permutations(m.keys()):
        current = 0
        for j in range(len(i)-1):
            current += m[i[j]][i[j+1]]
        result = current if current > result else result

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
