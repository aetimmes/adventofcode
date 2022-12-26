#!/usr/bin/python3.11
"""2015 day 19."""
from collections import defaultdict
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 19
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    rules, initial = data.split("\n\n")

    transitions: defaultdict[str, list[str]] = defaultdict(list)
    for line in lines(rules):
        ls, rs = line.split(" => ")
        transitions[rs].append(ls)

    target = "e"
    mols: set[str] = {initial}

    result = 0
    while target not in mols:
        next_mols = set()
        for mol in mols:
            for k, v in transitions.items():
                results: list[tuple[str, int]] = [("", 0)]
                tokens = mol.split(k)
                for i, t in enumerate(tokens):
                    next_submols = []
                    if i == len(tokens) - 1:
                        for (s, _) in [(r + t, c) for (r, c) in results if c == 1]:
                            next_mols.add(s)
                    else:
                        for (r, c) in results:
                            for e in v:
                                if c == 0:
                                    next_submols.append((r + t + e, c + 1))
                            next_submols.append((r + t + k, c))
                    results = next_submols
        mols = set(sorted(list(next_mols), key=len)[:1000])
        result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
