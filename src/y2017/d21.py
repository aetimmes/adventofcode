#!/usr/bin/python3.12
"""2017 day 21."""
from operator import methodcaller
from aocd.models import Puzzle

YEAR = 2017
DAY = 21

START = (
    ".#.",
    "..#",
    "###",
)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print(f"{data=}")
        rules = {}
        for line in data.split("\n"):
            ls, rs = [tuple(half.split("/")) for half in line.split(" => ")]
            for _ in range(2):
                for __ in range(4):
                    rules[ls] = rs
                    ls = tuple("".join(x) for x in zip(*ls[::-1]))
                ls = ls[::-1]

        current = START
        print(current)
        for _ in range(5):
            if len(current) % 2 == 0:
                inc = 2
            else:
                inc = 3
            n = []
            # iterate through top lefts
            for r in range(0, len(current), inc):
                for c in range(0, len(current), inc):
                    p = tuple(row[c:c+inc] for row in current[r:r+inc])
                    rule = rules[p]
                    for i in range(-len(rule), 0):
                        if c == 0:
                            n.append(rule[i])
                        else:
                            n[i] += rule[i]
            current = tuple(n)
            print(current)

        result = 0
        for r in current:
            for c in r:
                if c == "#":
                    result += 1
        return result

    def b(data):
        """Part b."""
        rules = {}
        for line in data.split("\n"):
            ls, rs = [tuple(half.split("/")) for half in line.split(" => ")]
            for _ in range(2):
                for __ in range(4):
                    rules[ls] = rs
                    ls = tuple("".join(x) for x in zip(*ls[::-1]))
                ls = ls[::-1]

        current = START
        print(current)
        for _ in range(18):
            if len(current) % 2 == 0:
                inc = 2
            else:
                inc = 3
            n = []
            # iterate through top lefts
            for r in range(0, len(current), inc):
                for c in range(0, len(current), inc):
                    p = tuple(row[c:c+inc] for row in current[r:r+inc])
                    rule = rules[p]
                    for i in range(-len(rule), 0):
                        if c == 0:
                            n.append(rule[i])
                        else:
                            n[i] += rule[i]
            current = tuple(n)
            print(current)

        result = 0
        for r in current:
            for c in r:
                if c == "#":
                    result += 1
        return result

    puzzle = Puzzle(year=YEAR, day=DAY)

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        try:
            answer = a(ex.input_data)
        except Exception as e:
            print("Example data exception: %s" % str(e))
            wrong = True
            answer = ""
        if str(answer) != ex.answer_a:
            print(f"Example data mismatch: {ex.answer_a=}, {answer=}")
            wrong = True

    if wrong and input("Example data mismatch; submit anyways? [y/N]:").lower().strip() != "y":
        exit()
    puzzle.answer_a = a(puzzle.input_data)

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        try:
            answer = b(ex.input_data)
        except Exception as e:
            print("Example data exception: %s" % str(e))
            wrong = True
            answer = ""
        if str(answer) != ex.answer_b:
            print(f"Example data mismatch: {ex.answer_b=}, {answer=}")
            wrong = True

    if wrong and input("Example data mismatch; submit anyways? [y/N]:").lower().strip() != "y":
        exit()
    puzzle.answer_b = b(puzzle.input_data)


if __name__ == "__main__":
    main()
