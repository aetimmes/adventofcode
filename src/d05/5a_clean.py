#!/usr/bin/python3.10
"""2022 day 5."""
from aocd import get_data, submit

YEAR = 2022
DAY = 5
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    (initial, commands) = (x.split("\n") for x in data.split("\n\n"))
    stacks = [
        [
            line[i * 4 + 1]
            for line in initial[-2::-1]
            if i * 4 + 1 < len(line) and line[i * 4 + 1] != " "
        ]
        for i in range(10)
    ]

    for line in commands:
        count, source, dest = map(int, line.split()[1::2])
        stacks[dest - 1].extend(stacks[source - 1][-count:][::-1])
        del stacks[source - 1][-count:]
    result = "".join([k[-1] for k in stacks if k])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
