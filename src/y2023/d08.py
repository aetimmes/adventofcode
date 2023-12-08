#!/usr/bin/python3.12
"""2023 day 8."""
import re
from math import lcm

from aocd.models import Puzzle

YEAR = 2023
DAY = 8

DIRECTIONS = {"L": 0, "R": 1}


def main():
    """Main."""

    def a(data):
        chunks = data.split("\n\n")
        result = 0

        steps = chunks[0].strip()
        m = {}
        for line in chunks[1].split("\n"):
            n, l, r = re.findall('[A-Z][A-Z][A-Z]', line, re.DOTALL)
            m[n] = [l, r]

        current = "AAA"
        while current != "ZZZ":
            current = m[current][DIRECTIONS[(steps[result % len(steps)])]]
            result += 1
        return result

    def b(data):
        """Part b."""
        chunks = data.split("\n\n")

        steps = chunks[0].strip()
        m = {n: [l, r] for n, l, r in (re.findall("[A-Z][A-Z][A-Z]", line, re.DOTALL) for line in chunks[1].split("\n"))}

        lengths = []
        for x in filter(lambda x: x[2] == "A", m):
            i = 0
            current = x
            while current[2] != "Z":
                current = m[current][DIRECTIONS[(steps[i % len(steps)])]]
                i += 1
            lengths.append(i)

        return lcm(*lengths)

    puzzle = Puzzle(year=YEAR, day=DAY)

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        answer = a(ex.input_data)
        if answer != ex.answer_a:
            print(f"Example data mismatch: {ex.answer_a=}, {answer=}")
            wrong = True

    if not wrong or input("Example data mismatch; submit anyways? [y/N]:").lower().strip() == "y":
        result = a(puzzle.input_data)
        print(f"{result=}")
        puzzle.answer_a = result

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        answer = a(ex.input_data)
        if answer != ex.answer_b:
            print(f"Example data mismatch: {ex.answer_b=}, {answer=}")
            wrong = True

    if not wrong or input("Example data mismatch; submit anyways? [y/N]:").lower().strip() == "y":
        result = b(puzzle.input_data)
        print(f"{result=}")
        puzzle.answer_b = result


if __name__ == "__main__":
    main()
