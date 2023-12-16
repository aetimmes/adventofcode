#!/usr/bin/python3.12
"""2023 day 16."""
from aocd.models import Puzzle

YEAR = 2023
DAY = 16

#  3
# 2 0
#  1

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

transitions = {
    ".": [(0,), (1,), (2,), (3,)],
    "/": [(3,), (2,), (1,), (0,)],
    "\\": [(1,), (0,), (3,), (2,)],
    "|": [(1, 3), (1,), (1, 3), (3,)],
    "-": [(0,), (0, 2), (2,), (0, 2)],
}


def boundscheck(r, c, mr, mc):
    return (0 <= r < mr) and (0 <= c < mc)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print("\n".join(data.splitlines()))
        grid = data.splitlines()

        stack = [((0, 0), 0)]
        seen = set()
        while stack:
            (r, c), d = stack.pop()
            if not boundscheck(r, c, len(grid), len(grid[0])):
                continue
            if ((r, c), d) in seen:
                continue
            seen.add(((r, c), d))
            for nd in transitions[grid[r][c]][d]:
                stack.append(((r + dirs[nd][0], c + dirs[nd][1]), nd))

        return len(set(x[0] for x in seen))

    def b(data):
        """Part b."""
        print("\n".join(data.splitlines()))
        result = 0
        grid = data.splitlines()

        starts = []
        for i in range(len(grid)):
            starts.append(((i, 0,), 0,))
            starts.append(((0, i,), 1,))
            starts.append(((i, len(grid) - 1,), 2,))
            starts.append(((len(grid) - 1, i,), 3,))
        for (ir, ic), i_d in starts:
            stack = [((ir, ic), i_d)]
            seen = set()
            while stack:
                (r, c), d = stack.pop()
                if not boundscheck(r, c, len(grid), len(grid[0])):
                    continue
                if ((r, c), d) in seen:
                    continue
                seen.add(((r, c), d))
                for nd in transitions[grid[r][c]][d]:
                    stack.append(((r + dirs[nd][0], c + dirs[nd][1]), nd))

            energized = len(set(x[0] for x in seen))
            result = max(result, energized)
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
