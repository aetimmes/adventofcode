#!/usr/bin/python3.10
"""2022 day 18."""
from itertools import chain
import itertools
from aocd import get_data, submit
from aocd.transforms import lines
from collections import deque

YEAR = 2022
DAY = 18
PART = "b"

deltas = list(
    chain.from_iterable(
        (
            (i, 0, 0),
            (0, i, 0),
            (0, 0, i),
        )
        for i in [1, -1]
    )
)


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elems = set()
    for line in data:
        elems.add(eval(line)) # pylint: disable=eval-used

    min_coord = 0 - 3
    max_coord = max(e[i] for e in elems for i in [0,1,2]) + 3

    result = set()
    seen = set()
    q = deque() 

    for x in range(max_coord+1):
        for y in [min_coord, max_coord]:
            for z in [min_coord, max_coord]:
                for p in itertools.permutations([x,y,z],3):
                    if p not in elems and p not in seen:
                        seen.add(p)
                        q.append(p)

    while q:
        current = q.popleft()
        for d in deltas:
            t = tuple(current[i] + d[i] for i in range(3))
            if not all(t[i] >= min_coord and t[i] <= max_coord for i in [0,1,2]):
                continue
            if t in elems:
                print(f"Found {t} from {current}")
                result.add((t,current))
            elif t not in seen:
                q.append(t)
                seen.add(t)

    print(f"{len(result)=}")
    submit(len(result), part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
