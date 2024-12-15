#!/usr/bin/env python3
"""2024 day 12."""
from collections import deque
from aocd.models import Puzzle
from copy import deepcopy

YEAR = 2024
DAY = 12

DS = {1,-1,1j,-1j}

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        m = dict()
        for r, line in enumerate(data.splitlines()):
            for c, cha in enumerate(line):
                m[r+c*1j] = cha
        om = deepcopy(m)
        result = 0
        while m:
            s = deque()
            (rc) = list(m.keys())[0]
            t = m.pop(rc)
            s.append(rc)
            a,p = 0,0
            while s:
                rc = s.pop()
                a+=1
                for d in DS:
                    if m.get(rc+d) == t:
                        s.append(rc+d)
                        m.pop(rc+d)
                    elif om.get(rc+d) != t:
                        p+=1
            result += a*p
        return result


    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))

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
