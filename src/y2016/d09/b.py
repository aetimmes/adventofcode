#!/usr/bin/python3.11
"""2016 day 9."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 9
PART = "b"


def main():
    """
    Part b.

    Core algorithm shamelessly stolen from the spoiler thread for this day. I couldn't
    figure out the right mental model to use for the expansions without storing the
    string in memory and every attempt I made at figuring out the math was wrong for at
    least one of the sample inputs.
    """
    data = "".join(lines(get_data(day=DAY, year=YEAR)))
    print(f"{data=}")

    mults = [1 for _ in data]
    result = 0
    i = 0
    while i < len(data):
        if data[i] == "(":
            start = i
            end = data.index(")", start) + 1
            chars, copies = tuple(map(int, data[start + 1:end - 1].split("x")))
            for j in range(end, end + chars):
                mults[j] *= copies
            i = end
        else:
            result += mults[i]
            i += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
