#!/usr/bin/python3.11
"""2017 day 10."""
from aocd import get_data, submit

YEAR = 2017
DAY = 10
PART = "b"


def main():
    """Part b."""
    data = [ord(t) for t in get_data(day=DAY, year=YEAR)] + [17, 31, 73, 47, 23]
    print(f"{data=}")

    elements = list(range(256))
    current = 0
    skip = 0
    for _ in range(64):
        for length in data:
            if length > len(elements):
                continue
            temp = elements + elements
            temp = (
                temp[0:current]
                + list(reversed(temp[current:current + length]))
                + temp[current + length:]
            )
            elements = (
                temp[(len(temp) // 2):len(temp) // 2 + current]
                + temp[current:len(temp) // 2]
            )
            current += length + skip
            current %= len(elements)
            skip += 1
            print(f"{elements=}")

    result = get_dense_hash(elements)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def get_dense_hash(elements):
    """Get the hex hash of a list of elements."""
    result = ""
    for i in range(16):
        chars = elements[i * 16:(i + 1) * 16]
        e = chars[0]
        for c in chars[1:]:
            e ^= c
        result += str(hex(e))[2:]
    return result


if __name__ == "__main__":
    main()
