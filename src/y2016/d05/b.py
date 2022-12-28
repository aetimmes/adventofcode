#!/usr/bin/python3.11
"""2016 day 5."""
import hashlib

from aocd import get_data, submit

YEAR = 2016
DAY = 5
PART = "b"


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = ["_" for _ in range(8)]
    index = 0

    while "_" in result:
        h = hashlib.md5((data + str(index)).encode("utf-8")).hexdigest()
        if h[:5] == "00000" and h[5] in "01234567" and result[int(h[5])] == "_":
            result[int(h[5])] = h[6]
        index += 1

    result = "".join(result)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
