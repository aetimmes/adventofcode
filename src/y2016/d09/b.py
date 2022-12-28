#!/usr/bin/python3.11
"""2016 day 9."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 9
PART = "b"


def decompress(s, i):
    ls, s = s[i:].split("(", 1)
    result = len(ls)
    if s:
        mid, s = s.split(")", 1)
        char_count, copy_count = tuple(map(int, mid.split("x")))
        score, s = decompress(s, i + char_count)
        result += copy_count * score
    return result, s


def main():
    """Part b."""
    data = "".join(lines(get_data(day=DAY, year=YEAR)))
    print(f"{data=}")

    result = 0

    while "(" in data:
        score, data = decompress(data, 0)
        result += score

    if data:
        decompressed += data

    result = len(decompressed)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
