#!/usr/bin/python3.12
"""2017 day 22."""
from aocd.models import Puzzle

YEAR = 2017
DAY = 22

DIRECTIONS = (
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1)   # left
)

def print_grid(infected, current):
    minr = min(x[0] for x in infected)
    maxr = max(x[0] for x in infected)
    minc = min(x[1] for x in infected)
    maxc = max(x[1] for x in infected)
    print(f"{current=}")
    for r in range(minr-1, maxr+2):
        row = ""
        for c in range(minc-1, maxc+2):
            if (r, c) in infected:
                if (r, c) == current:
                    row += "%"
                else:
                    row += "#"
            else:
                if (r, c) == current:
                    row += "^"
                else:
                    row += "."
        print(row)

def main():
    """Main."""

    def a(data):
        """Part a."""
        print(f"{data=}")
        infected = set()
        lines = data.splitlines()
        for r, l in enumerate(lines):
            for c, ch in enumerate(l):
                if ch == "#":
                    infected.add((r, c))

        pos = (len(lines)//2, len(lines)//2)
        d = 0
        result = 0
        for _ in range(10000):
            # print_grid(infected, pos)
            if pos in infected:
                d = (d+1) % 4
                infected.remove(pos)
            else:
                d = (d-1) % 4
                infected.add(pos)
                result += 1
            pos = (
                pos[0]+DIRECTIONS[d][0],
                pos[1]+DIRECTIONS[d][1]
            )
        return result


    def b(data):
        """Part b."""
        print(f"{data=}")
        infected = set()
        weakened = set()
        flagged = set()
        lines = data.splitlines()
        for r, l in enumerate(lines):
            for c, ch in enumerate(l):
                if ch == "#":
                    infected.add((r, c))

        pos = (len(lines)//2, len(lines)//2)
        d = 0
        result = 0
        for _ in range(10000000):
            # print_grid(infected, pos)
            if pos in infected:
                d = (d+1) % 4
                infected.remove(pos)
                flagged.add(pos)
            elif pos in weakened:
                weakened.remove(pos)
                infected.add(pos)
                result += 1
            elif pos in flagged:
                flagged.remove(pos)
                d = (d+2) % 4
            else:  # if clean
                weakened.add(pos)
                d = (d-1) % 4
            pos = (
                pos[0]+DIRECTIONS[d][0],
                pos[1]+DIRECTIONS[d][1]
            )
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
