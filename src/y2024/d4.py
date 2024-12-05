#!/usr/bin/env python3
"""2024 day 4."""
from aocd.models import Puzzle

YEAR = 2024
DAY = 4

DS = {
  (0,1),
  (1,0),
  (-1,0),
  (0,-1),
  (1,1),
  (1,-1),
  (-1,1),
  (-1,-1),
}

XS = {
    (1,1),
    (1,-1),
}

STR = 'XMAS'

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        d = {}
        for z in STR:
            d[z] = set()
        d['.'] = set() # stupid example input
        for i, l in enumerate(data.splitlines()):
            for j, c in enumerate(l):
                d[c].add((i,j,))
        result = 0
        for (x,y) in d['X']:
            for (dx, dy) in DS:
                if all((x+(i*dx), y+(i*dy),) in d[c] for (i, c) in enumerate(STR)):
                    result += 1
        return result


    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        d = {}
        for z in STR:
            d[z] = set()
        d['.'] = set() # stupid example input
        for i, l in enumerate(data.splitlines()):
            for j, c in enumerate(l):
                d[c].add((i,j,))
        result = 0
        for (x,y) in d['A']:
            if all(
                (
                    (x+ax,y+ay) in d['M'] and (x-ax,y-ay) in d['S']
                ) or (
                    (x+ax,y+ay) in d['S'] and (x-ax,y-ay) in d['M']
                )
                for (ax, ay) in XS
                ):
                result += 1
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
