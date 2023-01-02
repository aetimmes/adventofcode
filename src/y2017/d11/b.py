#!/usr/bin/python3.11
"""2017 day 11."""
from aocd import get_data, submit

YEAR = 2017
DAY = 11
PART = "b"

# Bug: I had nw and sw swapped in the order leading to misaggregated axial sums.
hex_dirs = [
    "n",
    "ne",
    "se",
    "s",
    "sw",
    "nw",
]


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split(",")
    print(f"{data=}")

    result = 0
    axes = [0 for _ in hex_dirs]
    for step in data:
        axes[hex_dirs.index(step)] += 1
        current = get_dist(axes)
        result = max(current, result)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def get_dist(axes):
    """Determine distance from a list of hex axes."""
    length = len(axes)
    print(f"{axes=}")
    for i in range(length):
        temp = min((axes[j] for j in (i, i - length // 2)))
        axes[i] -= temp
        axes[i - length // 2] -= temp

    print(f"{axes=}")
    # Bug: I originally had this set to sys.maxsize, which breaks when we're standing
    # at the origin and the array index is wildly out of bounds. Instead, we use 0,
    # since if we don't find an edge, it means 4+ of the elements are 0, so the
    # subtraction is a noop.
    right_edge = 0
    for i in range(length):
        if axes[i] and axes[i - 1] and axes[i - 2]:
            right_edge = i
    temp = min(axes[right_edge - i] for i in (0, 2))
    axes[right_edge] -= temp
    axes[right_edge - 1] += temp
    axes[right_edge - 2] -= temp

    result = sum(axes)
    return result


if __name__ == "__main__":
    main()
