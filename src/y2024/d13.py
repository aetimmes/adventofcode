#!/usr/bin/env python3
"""2024 day 13."""
import re
from z3 import *
from aocd.models import Puzzle

YEAR = 2024
DAY = 13

C = 10000000000000

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        for chunk in data.split("\n\n"):
            c = []
            for line in chunk.splitlines():
                c.append(list(map(int, (re.findall(r'\d+', line)))))
            o = Optimize()
            a = Int('a')
            b = Int('b')
            o.add(c[0][0] * a + c[1][0] * b == c[2][0])
            o.add(c[0][1] * a + c[1][1] * b == c[2][1])
            o.minimize(3*a+b)
            if o.check() == z3.sat:
                m = o.model()
                result += 3*(m[a].as_long()) + (m[b].as_long())
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        for chunk in data.split("\n\n"):
            c = []
            for line in chunk.splitlines():
                c.append(list(map(int, (re.findall(r'\d+', line)))))
            o = Optimize()
            a = Int('a')
            b = Int('b')
            o.add(c[0][0] * a + c[1][0] * b == c[2][0] + C)
            o.add(c[0][1] * a + c[1][1] * b == c[2][1] + C)
            o.minimize(3*a+b)
            if o.check() == z3.sat:
                m = o.model()
                result += 3*(m[a].as_long()) + (m[b].as_long())
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
