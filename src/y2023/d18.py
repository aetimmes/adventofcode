#!/usr/bin/python3.12
"""2023 day 18."""
from copy import deepcopy
from aocd.models import Puzzle

YEAR = 2023
DAY = 18

DIRS = {
    "R": (0,1),
    "L": (0,-1),
    "U": (-1,0),
    "D": (1,0)
}

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        p = (0,0)
        dug = set()
        for line in data.splitlines():
            d, c = line.split()[:2]
            c = int(c)
            for _ in range(c):
                dug.add(p)
                p = (p[0] + DIRS[d][0], p[1] + DIRS[d][1])
        dug.add(p)

        min_r = min(x[0] for x in dug)
        min_c = min(x[1] for x in dug)
        max_r = max(x[0] for x in dug)
        max_c = max(x[1] for x in dug)

        outside = set()
        orig_dug = deepcopy(dug)
        for r, c in orig_dug:
            for d in DIRS.values():
                seen = set()
                bad = False
                nr, nc = (r+d[0], c+d[1])
                stack = [(nr, nc)]
                print("checking new stack", stack[-1])
                while stack and not bad:
                    current = stack.pop()
                    print("checking", current)
                    (nr, nc) = current
                    if current in dug:
                        print(current, "dug")
                        continue
                    if current in seen:
                        print(current, "seen")
                        continue
                    seen.add(current)
                    if (nr < min_r) or (nr > max_r) or (nc < min_c) or (nc > max_c):
                        print(current, "new outside")
                        outside = outside.union(seen)
                        bad = True
                        break
                    if (nr,nc) in outside:
                        print(current, "existing outside")
                        outside = outside.union(seen)
                        bad = True
                        break
                    for nd in DIRS.values():
                        stack.append((nr+nd[0], nc+nd[1]))
                if not bad:
                    print(current, "inside")
                    dug = dug.union(seen)
        
        print(f"{min_r=}, {max_r=}, {min_c=}, {max_c=}")
        for r in range(min_r, max_r+1):
            row = ""
            for c in range(min_c, max_c+1):
                if (r, c) in dug:
                    row += "#"
                else:
                    row += "."
            print(row)


        return len(dug)




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
