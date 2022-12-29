#!/usr/bin/python3.11
"""2016 day 24."""
import itertools
import sys
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 24
PART = "b"

DELTAS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    spaces = set()
    interest = set()
    distances = defaultdict(dict)

    for r, line in enumerate(data):
        for c, cha in enumerate(line):
            if cha != "#":
                spaces.add((r, c))
            if cha == "0":
                start = (r, c)
            if cha in "0123456789":
                interest.add((r, c))

    for src in interest:
        for dst in interest:
            if src == dst:
                continue
            q = [src]
            seen = set(src)
            found = False
            steps = 0
            while not found:
                steps += 1
                next_ = []
                while q:
                    curr = q.pop()
                    for d in DELTAS:
                        new_pos = (curr[0] + d[0], curr[1] + d[1])
                        if new_pos in spaces and new_pos not in seen:
                            if new_pos == dst:
                                found = True
                                break
                            next_.append(new_pos)
                            seen.add(new_pos)
                q = next_
            distances[src][dst] = steps

    print(f"{distances=}")

    interest.remove(start)

    result = sys.maxsize
    for perm in itertools.permutations(interest):
        current = distances[start][perm[0]]
        for i in range(len(perm) - 1):
            current += distances[perm[i]][perm[i + 1]]
        current += distances[perm[-1]][start]
        if current < result:
            result = current

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
