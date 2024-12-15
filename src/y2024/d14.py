#!/usr/bin/env python3
"""2024 day 14."""
import re
from aocd.models import Puzzle

YEAR = 2024
DAY = 14

X = 101
Y = 103

def main():
    """Main."""

    def a(data):
        """Part a."""
        #print('\n'.join(data.splitlines()))
        rs = [0,0,0,0]

        for line in data.splitlines():
            ns = list(map(int, re.findall(r'-*\d+',line)))
            x = (ns[0] + 100*ns[2]) % X
            y = (ns[1] + 100*ns[3]) % Y
            i = 0
            if (x == (X//2)) or (y == (Y//2)):
                print(line, f"{x=},{y=},SKIP")
                continue
            else:
                if x >= (X//2):
                    i+=1
                if y >= (Y//2):
                    i+=2
                print(line, f"{x=},{y=},{i=}")
                rs[i] += 1
        result = 1
        print(rs)
        for r in rs:
            result *= r
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        robots = []
        for line in data.splitlines():
            robots.append(list(map(int, re.findall(r'-*\d+',line))))
        result = 0
        done = False
        while not done:
            result += 1 
            s = set()
            for i, r in enumerate(robots):
                x = (r[0]+r[2]) % X
                y = (r[1]+r[3]) % Y
                robots[i] = [x,y,r[2],r[3]]
                s.add((x,y))
            for x in range(X):
                l = ''
                for y in range(Y):
                    if (x,y) in s:
                        l += '#'
                    else:
                        l += '.'
                print(l)
            # I didn't actually do this; instead I eyeballed interesting periods of vertical/horizontal arrangement,
            # noted the periodicity, and figured out where the cycles synced for the first time
            if input(f"iteration {result}: Is this a christmas tree?") == 'y':
                done = True
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
