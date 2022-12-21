#!/usr/bin/python3.10
"""2022 day 16."""
from collections import defaultdict
from pprint import pprint
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 16
PART = "b"


TIME_LIMIT = 26


def main():
    """Part b."""
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
    if flow_rates["AA"] == 0:
        working_valves.remove("AA")
    result = 0

    def descent(person, elephant, valves):
        results = []
        for target in [person, elephant]:
            (cloc, ctime, score) = target[-1]
            for valve in valves:
                ptime = ctime + distances[cloc][valve] + 1
                if ptime <= TIME_LIMIT:
                    valves.remove(valve)
                    target.append(
                        (
                            valve,
                            ptime,
                            score + (flow_rates[valve] * (TIME_LIMIT - ptime)),
                        )
                    )
                    results.append(descent(person, elephant, valves))
                    target.pop()
                    valves.add(valve)
        if not results:
            return person[-1][-1] + elephant[-1][-1]
        return max(results)

    person = [("AA", 0, 0)]
    elephant = [("AA", 0, 0)]

    result = descent(person, elephant, working_valves)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
