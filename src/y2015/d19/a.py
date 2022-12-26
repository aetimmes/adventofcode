#!/usr/bin/python3.11
"""2015 day 19."""
from collections import defaultdict
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 19
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    rules, initial = data.split("\n\n")

    transitions: defaultdict[str, list[str]] = defaultdict(list)
    for line in lines(rules):
        ls, rs = line.split(" => ")
        transitions[ls].append(rs)

    mols: set[str] = set()

    for k, v in transitions.items():
        results: list[tuple[str, int]] = [("", 0)]
        tokens = initial.split(k)
        for i, t in enumerate(tokens):
            next_ = []
            if i == len(tokens) - 1:
                next_ = [(r + t, c) for (r, c) in results]
            else:
                for (r, c) in results:
                    for e in v:
                        if c == 0:
                            next_.append((r + t + e, c + 1))
                    next_.append((r + t + k, c))
            results = next_
        for (s, c) in results:
            if c == 1:
                mols.add(s)

    result = len(mols)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
