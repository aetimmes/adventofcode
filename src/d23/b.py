#!/usr/bin/python3.11
"""2022 day 23."""
from collections import defaultdict
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 23
PART = "b"

# (r, c) format, (0, 0) is top-left

order = "NSWE"

directions = {
    "N": (-1, 0),
    "S": (1, 0),
    "W": (0, -1),
    "E": (0, 1),
    "NW": (-1, -1),
    "SW": (1, -1),
    "NE": (-1, 1),
    "SE": (1, 1),
}


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elves = set()
    for r, line in enumerate(data):
        for c, char in enumerate(line):
            if char == "#":
                elves.add((r, c))
    num_elves = len(elves)
    i = 0
    while True:
        proposals = defaultdict(set)
        r_proposals = {}
        for (r, c) in elves:
            if all((r + v[0], c + v[1]) not in elves for v in directions.values()):
                continue
            for j in range(len(order)):
                d = order[(i + j) % 4]
                if all(
                    ((r + v[0], c + v[1]) not in elves)
                    for k, v in directions.items()
                    if d in k
                ):
                    proposals[(r + directions[d][0], c + directions[d][1])].add((r, c))
                    r_proposals[(r, c)] = (r + directions[d][0], c + directions[d][1])
                    break
        if len(proposals) == 0:
            break
        for (r, c) in list(elves):
            if proposals.get(r_proposals.get((r, c))) == {(r, c)}:
                elves.remove((r, c))
                if r_proposals[(r, c)] in elves:
                    raise ValueError(
                        f"Trying to add duplicate elf at {r_proposals[(r, c)]}"
                    )
                elves.add(r_proposals[(r, c)])
            if len(elves) != num_elves:
                raise ValueError(
                    f"Elf count mismatch: expected {num_elves}, got {len(elves)}"
                )
        print_grid(elves)
        i += 1

    result = i+1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def print_grid(elves):
    """Print the elf grid."""
    (min_r, min_c) = (min(e[i] for e in elves) for i in [0, 1])
    (max_r, max_c) = (max(e[i] for e in elves) for i in [0, 1])
    grid = []
    for r in range(min_r, max_r + 1):
        line = ""
        for c in range(min_c, max_c + 1):
            line += "#" if (r, c) in elves else "."
        grid.append(line)
    print("\n".join(grid))
    return grid


if __name__ == "__main__":
    main()
