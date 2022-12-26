#!/usr/bin/python3.11
"""2015 day 15."""
import math
from aocd import get_data, submit
from aocd.transforms import lines
from numpy import array

YEAR = 2015
DAY = 15
PART = "b"

LIMIT = 100


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    ingredients = []

    for line in data:
        ingredients.append(
            array(
                [
                    int(t.split(",")[0])
                    for i, t in enumerate(line.split())
                    if i in [2, 4, 6, 8, 10]
                ]
            )
        )

    result = 0
    amounts = None
    for i in range(LIMIT):
        for j in range(LIMIT - i):
            for k in range(LIMIT - i - j):
                m = LIMIT - i - j - k
                counts = array([i, j, k, m])
                scores = array([0, 0, 0, 0, 0])
                for x, ingredient in enumerate(ingredients):
                    scores += ingredient * counts[x]
                if scores[-1] != 500:
                    continue
                score = math.prod(max(0, s) for s in scores[:-1])
                if score > result:
                    amounts = counts
                    result = score

    print(f"{result=}")
    print(f"{amounts=}")
    submit(int(result), part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
