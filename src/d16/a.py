#!/usr/bin/python3.10
"""2022 day 16."""
import sys
from collections import defaultdict
from pprint import pprint

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 16
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    flow_rates = {}
    dests = {}

    for line in data:
        tokens = line.split()
        name = tokens[1]
        flow_rates[name] = int(tokens[4].split("=")[1][0:-1])
        dests[name] = [t[0:2] for t in tokens[9:]]

    distances = defaultdict(dict)

    working_valves: set[str] = {k for k, v in flow_rates.items() if v > 0}
    working_valves.add("AA")

    for v in working_valves:
        cands = {x for x in working_valves if x is not v and not distances[v].get(x)}
        t = 0
        queue = [v]
        nq = []
        seen = set()
        while cands:
            while queue:
                curr = queue.pop(0)
                seen.add(curr)
                if curr in cands:
                    cands.remove(curr)
                    distances[v][curr] = t
                    distances[curr][v] = t
                for dest in dests[curr]:
                    if dest not in seen:
                        nq.append(dest)
            queue = nq
            nq = []
            t += 1

    pprint(distances)

    result: tuple[int, ...] = (0,)
    if flow_rates["AA"] == 0:
        working_valves.remove("AA")

    # loc, open valves, time
    dfs: list[tuple[str, set[str], int, tuple[int, ...], tuple[str, ...]]] = [
        ("AA", set(), 0, (0,), tuple())  # loc  # open_valves  # t  # scores  # path
    ]

    winning_path = []

    while dfs:
        elem = dfs.pop(0)
        loc, open_valves, t, scores, path = elem

        if len(scores) != t + 1:
            print(f"broken {elem=}")
        increment = sum(flow_rates[v] for v in open_valves)
        scores = scores + (scores[-1] + increment,)
        if t >= 30:
            continue
        if scores[-1] > result[-1]:
            result = scores
            winning_path = path
        if loc in working_valves and loc not in open_valves:
            dfs.insert(
                0, (loc, open_valves | {loc}, t + 1, scores + tuple(), path + (loc,))
            )
            continue

        if (
            min(
                [distances[loc][x] for x in working_valves if x not in open_valves]
                + [sys.maxsize]
            )
            + t
            >= 30
        ):
            for _ in range(t + 1, 30):
                scores = scores + (scores[-1] + increment,)
            if len(scores) != 31:
                print("broken!!!")
                return
            if scores[-1] > result[-1]:
                result = scores
                winning_path = path
        else:
            for x in working_valves:
                if x not in open_valves and x != loc:
                    dist = distances[loc][x]
                    new_scores = scores
                    for _ in range(dist - 1):
                        new_scores += (new_scores[-1] + increment,)
                    dfs.insert(0, (x, open_valves, t + dist, new_scores, path))

    print(f"{result=}")
    print(f"{len(result)=}")
    print(f"{winning_path=}")
    print(f"{len(winning_path)=}")
    if len(result) == 31:
        submit(result[-1], part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
