#!/usr/bin/env python3
"""2024 day 3."""
import re
from aocd.models import Puzzle

YEAR = 2024
DAY = 3


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        regex = 'mul\((\d{1,3}),(\d{1,3})\)'
        for line in data.splitlines():
            for m in re.findall(regex, line):
                result += (int(m[0]) * int(m[1]))
        return result


    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        regex = 'mul\((\d{1,3}),(\d{1,3})\)'
        for segment in ''.join(data.splitlines()).split('do()'):
            for m in re.findall(regex, segment.split('don\'t()')[0]):
                result += (int(m[0]) * int(m[1]))
        return result

    puzzle = Puzzle(year=YEAR, day=DAY)

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[part](ex.input_data)
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
        answer = locals()[part](puzzle.input_data)
        print(f"{answer=}")
        setattr(puzzle, f"answer_{part}", answer)


if __name__ == "__main__":
    main()
