#!/usr/bin/python3.11
"""2023 day 5b."""
from aocd import get_data, submit

YEAR = 2023
DAY = 5
PART = "b"


def main():
    """Part b."""
    chunks = get_data(day=DAY, year=YEAR).split("\n\n")
    seeds = [int(t) for t in chunks[0].split(": ")[1].split()]
    ranges = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

    maps = [
        [[int(t) for t in line.split()] for line in chunk.split("\n")[1:]]
        for chunk in chunks[1:]
    ]

    result = -1
    while True:
        result += 1
        print(f"trying {result}")
        current = result
        for m in maps[::-1]:
            for dst, src, rng in m:
                if dst <= current < dst + rng:
                    current -= dst
                    current += src
                    break
        for r in ranges:
            if r[0] <= current < r[0] + r[1]:
                print(f"{result=}")
                submit(result, part=PART, day=DAY, year=YEAR)
                exit()


if __name__ == "__main__":
    main()
