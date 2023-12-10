#!/usr/bin/python3.12
"""2023 day FIXME."""
from aocd.models import Puzzle

YEAR = 2023
DAY = -1  # FIX ME


def main():
    """Main."""

    def a(data):
        """Part a."""
        print(f"{data=}")

    def b(data):
        """Part b."""
        print(f"{data=}")

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

    if (
        wrong
        and input("Example data mismatch; submit anyways? [y/N]:").lower().strip()
        != "y"
    ):
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

    if (
        wrong
        and input("Example data mismatch; submit anyways? [y/N]:").lower().strip()
        != "y"
    ):
        exit()
    puzzle.answer_b = b(puzzle.input_data)


if __name__ == "__main__":
    main()
