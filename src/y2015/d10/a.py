#!/usr/bin/python3.11
"""2015 day 10."""
from aocd import get_data, submit

YEAR = 2015
DAY = 10
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    prev = data
    for _ in range(40):
        current = ""
        next_ = ""
        count = 0
        for c in prev:
            if c != current:
                if current:
                    next_ += str(count) + current
                current = c
                count = 1
                continue
            else:
                count += 1
        if count:
            next_ += str(count) + current
        prev = next_

    result = len(prev)

    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
