#!/usr/bin/env python3
"""2024 day 6."""
from collections import defaultdict
from aocd.models import Puzzle

YEAR = 2024
DAY = 6

# r,c
DS = [
  (-1,0), # N
  (0,1), # E
  (1,0), # S
  (0,-1),# W
]

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        seen = set()
        m = dict()
        d = 0
        for i, line in enumerate(data.splitlines()):
            for j, c in enumerate(line):
                if c == '^':
                    (x,y) = (i,j)
                    c = '.'
                m[(i,j,)] = c

        while (x,y,) in m:
            seen.add((x,y,))
            while m.get((x+DS[d][0],y+DS[d][1],)) == '#':
                d = (d + 1) % 4
            x += DS[d][0]
            y += DS[d][1]

        return len(seen)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        seen = set()
        m = dict()
        for i, line in enumerate(data.splitlines()):
            for j, c in enumerate(line):
                if c == '^':
                    (ox,oy) = (i,j)
                    c = '.'
                m[(i,j,)] = c

        x,y,d = ox,oy,0
        while (x,y,) in m:
            seen.add((x,y,))
            while m.get((x+DS[d][0],y+DS[d][1],)) == '#':
                d = (d + 1) % 4
            x += DS[d][0]
            y += DS[d][1]

        for (px,py) in seen:
            if (px,py) == (ox,oy):
                continue
            m[(px,py)] = '#'
            cseen = defaultdict(lambda: set())
            x,y,d = ox,oy,0
            while (x,y,) in m:
                if d in cseen[(x,y,)]:
                    result += 1
                    m[(px,py)] = '.'
                    break
                cseen[(x,y,)].add(d)
                while m.get((x+DS[d][0],y+DS[d][1],)) == '#':
                    d = (d + 1) % 4
                x += DS[d][0]
                y += DS[d][1]

            m[(px,py)] = '.'
        
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
