#!/usr/bin/python3.12
"""2023 day 9."""
from aocd.models import Puzzle

YEAR = 2023
DAY = 9


def main():
    """Main."""

    def a(data):
        """Part a."""
        lines = data.split("\n")
        result = 0
        for line in lines:
            pyramid = [[int(x) for x in line.split()]]
            while pyramid[-1] != [0] * len(pyramid[-1]):
                pyramid.append([pyramid[-1][i+1] - pyramid[-1][i] for i in range(len(pyramid[-1])-1)])
            result += sum(p[-1] for p in pyramid)
        return result


    def b(data):
        """Part b."""
        lines = data.split("\n")
        result = 0
        for line in lines:
            pyramid = [[int(x) for x in line.split()]]
            while pyramid[-1] != [0] * len(pyramid[-1]):
                pyramid.append([pyramid[-1][i+1] - pyramid[-1][i] for i in range(len(pyramid[-1])-1)])
            current = 0
            for p in pyramid[::-1]:
                current = p[0] - current
            result += current
        return result

    puzzle = Puzzle(year=YEAR, day=DAY)

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        answer = a(ex.input_data)
        if str(answer) != ex.answer_a:
            print(f"Example data mismatch: {ex.answer_a=}, {answer=}")
            wrong = True

    if wrong and input("Example data mismatch; submit anyways? [y/N]:").lower().strip() != "y":
        exit()
    puzzle.answer_a = a(puzzle.input_data)

    wrong = False
    for i, ex in enumerate(puzzle.examples):
        answer = b(ex.input_data)
        if str(answer) != ex.answer_b:
            print(f"Example data mismatch: {ex.answer_b=}, {answer=}")
            wrong = True

    if wrong and input("Example data mismatch; submit anyways? [y/N]:").lower().strip() != "y":
        exit()
    puzzle.answer_b = b(puzzle.input_data)


if __name__ == "__main__":
    main()
