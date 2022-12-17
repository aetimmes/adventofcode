#!/usr/bin/python3.10
"""2022 day 16."""
from collections import defaultdict
import copy
from itertools import permutations
from pprint import pprint
import sys
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 16
PART = "b"

DATA = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

TIME_LIMIT = 26


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    # data = DATA.splitlines()
    print(f"{data=}")

    flow_rates = {}
    dests = {}

    for line in data:
        tokens = line.split()
        name = tokens[1]
        flow_rates[name] = int(tokens[4].split("=")[1][0:-1])
        dests[name] = [t[0:2] for t in tokens[9:]]

    distances = defaultdict(dict)

    working_valves: set[str] = {v for v in flow_rates if flow_rates[v] > 0}
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

    dfs: list[
        tuple[
            tuple[str, str],
            tuple[int, int],
            int,
            tuple[int, ...],
            set[str],
            tuple[tuple[str, ...], tuple[str, ...]],
        ]
    ] = [(("AA", "AA"), (-1, -1), 0, (0,), set(), (tuple(), tuple()))]
    winning_paths = []

    while dfs:
        elem = dfs.pop(0)
        (destinations, travel_times, time, scores, ovs, paths) = elem
        open_valves = copy.deepcopy(ovs)
        increment = sum(flow_rates[l] for l in open_valves)

        while time < TIME_LIMIT and all(tt > 0 for tt in travel_times):
            scores = scores + (scores[-1] + increment,)
            time += 1
            travel_times = tuple([tt - 1 for tt in travel_times])

        if len(scores) != time + 1:
            print(f"broken {elem=}")

        if time >= TIME_LIMIT:
            if scores[-1] > result[-1]:
                result = scores
                winning_paths = paths
            continue

        if any(
            tt == 0 and destinations[i] in working_valves
            for i, tt in enumerate(travel_times)
        ):
            scores = scores + (scores[-1] + increment,)
            time += 1
            travel_times = tuple([tt - 1 for tt in travel_times])
            for i in [0, 1]:
                if travel_times[i] == -1:
                    open_valves.add(destinations[i])
            if time >= TIME_LIMIT:
                if scores[-1] > result[-1]:
                    winning_paths = paths
                    result = scores
                continue

        potential_distances = [
            distances[a][b]
            for i, a in enumerate(destinations)
            if travel_times[i] == -1
            for b in working_valves
            if b not in open_valves and b not in destinations and b != a
        ]

        min_dist = min(potential_distances + [sys.maxsize])

        if time + min_dist > TIME_LIMIT:
            tts = list(travel_times)
            ds = list(destinations)
            for i in [0, 1]:
                if tts[i] == -1:
                    tts[i] = 99
                    ds[i] = "waiting"
            dfs.insert(0, (tuple(ds), tuple(tts), time, scores, open_valves, paths))

        else:
            for p in permutations(
                [d for d in working_valves if d not in open_valves], 2
            ):
                tts = list(travel_times)
                ds = list(destinations)
                ps = []
                for i in [0, 1]:
                    if tts[i] == -1:
                        tts[i] = distances[ds[i]][p[i]]
                        ds[i] = p[i]
                        ps.append(paths[i] + (p[i],))
                    else:
                        ps.append(paths[i])
                dfs.append(
                    (tuple(ds), tuple(tts), time, scores, open_valves, tuple(ps))
                )

    print(f"{result=}")
    print(f"{len(result)=}")
    print(f"{winning_paths=}")
    print(f"{len(winning_paths)=}")

    if len(result) == 31:
        submit(result[-1], part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
