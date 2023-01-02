#!/usr/bin/python3.11
"""2017 day 14."""
from aocd import get_data, submit

YEAR = 2017
DAY = 14
PART = "b"

DELTAS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    hashes = []
    for i in range(128):
        hashes.append(get_knot_hash(f"{data}-{i}"))

    ones = set()
    for r, line in enumerate(hashes):
        for i, num in enumerate(line):
            for j, e in enumerate(f"{num:08b}"):
                if e == "1":
                    ones.add((r, i * 8 + j))

    print_grid(ones)

    result = 0
    while ones:
        result += 1
        q = [ones.pop()]
        while q:
            (r, c) = q.pop()
            for dr, dc in DELTAS:
                e = (r + dr, c + dc)
                if e in ones:
                    q.append(e)
                    ones.remove(e)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def print_grid(ones):
    """Print a representation of a hash grid."""
    grid = []
    for r in range(128):
        current = ""
        for c in range(128):
            if (r, c) in ones:
                current += "#"
            else:
                current += "."
        grid.append(current)
    for line in grid:
        print(line)


def get_knot_hash(input_string):
    """Get the knot hash of an input string."""
    lengths = [ord(c) for c in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    elements = list(range(256))
    current = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
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

    result = get_dense_hash(elements)
    return result


def get_dense_hash(elements):
    """Get the hex hash of a list of elements."""
    result = []
    for i in range(16):
        chars = elements[i * 16:(i + 1) * 16]
        e = chars[0]
        for c in chars[1:]:
            e ^= c
        result.append(e)
    return result


if __name__ == "__main__":
    main()
