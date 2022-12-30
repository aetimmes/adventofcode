#!/usr/bin/python3.11
"""2017 day 7."""
import itertools
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 7
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    parents = {}
    children = {}
    weights = {}
    for line in data:
        tokens = line.split(" -> ")
        ls = tokens[0]
        (nodename, weight) = ls.split()
        weights[nodename] = int(weight[1:-1])
        if len(tokens) == 2:
            rs = tokens[1]
            children[nodename] = rs.split(", ")
            for child in children[nodename]:
                parents[child] = nodename

    root = [node for node in weights if node not in parents][0]

    cumulative_weights = defaultdict(int)

    for node, weight in weights.items():
        cumulative_weights[node] += weight
        current = node
        while parents.get(current):
            current = parents[current]
            cumulative_weights[current] += weight
    bad = ""
    q = [root]
    while q:
        current = q.pop()
        suspects = set(children[current])
        for (a, b) in itertools.combinations(suspects, 2):
            if cumulative_weights[a] == cumulative_weights[b]:
                suspects.discard(a)
                suspects.discard(b)
        for s in suspects:
            q.append(s)
        if not suspects:
            print(current)
            bad = current

    bad_siblings = children[parents[bad]]
    bad_siblings.remove(bad)
    diff = cumulative_weights[bad_siblings[0]] - cumulative_weights[bad]
    result = weights[bad] + diff
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
