#!/usr/bin/python3.11
"""2017 day 6."""
from aocd import get_data, submit

YEAR = 2017
DAY = 6
PART = "b"


def main():
    """Part b."""
    data = [int(x) for x in get_data(day=DAY, year=YEAR).split()]
    print(f"{data=}")
    seen = set()
    for _ in [1, 2]:
        seen = set()
        while tuple(data) not in seen:
            seen.add(tuple(data))
            i = data.index(max(data))
            to_distribute = data[i]
            data[i] = 0
            for _ in range(to_distribute):
                i += 1
                i %= len(data)
                data[i] += 1

    result = len(seen)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
