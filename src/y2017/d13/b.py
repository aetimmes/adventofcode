#!/usr/bin/python3.11
"""2017 day 13."""
from collections import defaultdict
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 13
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")
    mods = defaultdict(set)
    ranges = {}
    for line in data:
        ls, rs = (int(t) for t in line.split(": "))
        period = 2 * (rs - 1)
        unsafe = -ls % period
        ranges[ls] = rs
        mods[period].add(unsafe)

    for m in sorted(mods):
        for n in sorted(mods):
            if m != n and n % m == 0:
                salt = 0
                while salt <= n:
                    for mod in mods[m]:
                        mods[n].add(mod + salt)
                    salt += m
    inverse_mods = {m: {i for i in range(m) if i not in mods[m]} for m in mods}

    result = 0
    while True:
        if all((result % k) in v for k, v in inverse_mods.items()):
            break
        result += 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
