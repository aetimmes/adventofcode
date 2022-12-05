#!/usr/bin/python3.10
"""2022 day 5."""
from aocd import get_data, submit

YEAR = 2022
DAY = 5
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")
    stacks: list[list[str]] = []
    initial_lines = []
    initialized = False
    for line in data:
        if not initialized and line:
            initial_lines.append(line)
        elif not initialized:
            buckets = len(initial_lines[-1].split())
            stacks = [[] for _ in range(buckets)]
            initial_lines.pop()  # get rid of unneeded line
            for i_l in initial_lines:
                for i in range(buckets):
                    if i_l[4 * i + 1] != " ":
                        stacks[i].insert(0, i_l[4 * i + 1])
            print(f"{stacks=}")
            initialized = True
        else:
            tokens = line.split()
            count, source, dest = int(tokens[1]), int(tokens[3]) - 1, int(tokens[5]) - 1
            for _ in range(count):
                stacks[dest].append(stacks[source].pop())

    result = "".join([k[-1] for k in stacks if k])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
