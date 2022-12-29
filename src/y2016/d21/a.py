#!/usr/bin/python3.11
"""2016 day 21."""
from collections import deque

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 21
PART = "a"

directions = {"left": -1, "right": 1}


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")
    word: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for line in data:
        tokens = line.split()
        if tokens[0] == "swap":
            if tokens[1] == "position":
                x, y = int(tokens[2]), int(tokens[-1])
            else:
                x, y = word.index(tokens[2]), word.index(tokens[-1])
            word[x], word[y] = word[y], word[x]
        if tokens[0] == "rotate":
            d = deque(word)
            if tokens[1] in directions:
                d.rotate(directions[tokens[1]] * int(tokens[-2]))
            else:
                i = word.index(tokens[-1])
                if i >= 4:
                    i += 1
                d.rotate(i + 1)
            word = list(d)
        if tokens[0] == "reverse":
            x, y = int(tokens[2]), int(tokens[-1])
            word = word[:x] + list(reversed(word[x : y + 1])) + word[y + 1 :]
        if tokens[0] == "move":
            x, y = int(tokens[2]), int(tokens[-1])
            word.insert(y, word.pop(x))

    result = "".join(word)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
