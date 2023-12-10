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

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals[part](ex.input_data)
                if (str(answer) != getattr(ex, f"answer_{part}")) and input(
                    f"Example data mismatch: {getattr(ex, f'answer_{part}')=}, {answer=}; submit anyways? [y/N]:"
                ).lower().strip() != "y":
                    exit()
            except Exception as e:
                print("Example data exception: %s" % str(e))
                if (
                    input("Example data exception; submit anyways? [y/N]:")
                    .lower()
                    .strip()
                    != "y"
                ):
                    raise

        setattr(puzzle, f"answer_{part}", locals()[part](puzzle.input_data))


if __name__ == "__main__":
    main()
