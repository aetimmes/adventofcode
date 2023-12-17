#!/usr/bin/python3.12
"""2023 day 17."""
from aocd.models import Puzzle
from collections import deque

YEAR = 2023
DAY = 17

# N
# W E
# S

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))  # NESW

MAX = 9999999999

def boundscheck(r, c, mr, mc):
    return (0 <= r < mr) and (0 <= c < mc)


def main():
    """Main."""

    def a(data):
        """Part a."""
        print("\n".join(data.splitlines()))
        grid = data.splitlines()
        mins = {}
        q = deque([])
        q.append(((0, 1), 0, 1, 1))  # (r,c), heat_loss, dir, dir_count
        q.append(((1, 0), 0, 2, 1))  # (r,c), heat_loss, dir, dir_count
        result = MAX 
        while q:
            (r, c), heat_loss, d, dc = q.popleft()
            if not boundscheck(r, c, len(grid), len(grid[0])):
                continue
            heat_loss += int(grid[r][c])
            if mins.get((r, c, d, dc), MAX) <= heat_loss:
                continue
            mins[(r, c, d, dc)] = heat_loss
            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                if heat_loss < result:
                    print(f"new min: {heat_loss=}")
                result = min(result, heat_loss)
                continue
            if dc != 3:
                next_dirs = (((d + i) % 4) for i in (-1, 0, 1))
            else:
                next_dirs = (((d + i) % 4) for i in (-1, 1))
            for nd in next_dirs:
                q.append(((r + DIRS[nd][0], c + DIRS[nd][1]), heat_loss, nd, 1 if nd != d else dc+1))
        print(result)
        return result

    def b(data):
        """Part b."""
        print("\n".join(data.splitlines()))
        grid = data.splitlines()
        mins = {}
        q = deque([])
        q.append(((0, 1), 0, 1, 1))  # (r,c), heat_loss, dir, dir_count
        q.append(((1, 0), 0, 2, 1))  # (r,c), heat_loss, dir, dir_count
        result = MAX 
        while q:
            (r, c), heat_loss, d, dc = q.popleft()
            if not boundscheck(r, c, len(grid), len(grid[0])):
                continue
            heat_loss += int(grid[r][c])
            if mins.get((r, c, d, dc), MAX) <= heat_loss:
                continue
            mins[(r, c, d, dc)] = heat_loss
            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                if heat_loss < result:
                    print(f"new min: {heat_loss=}")
                result = min(result, heat_loss)
                continue
            if dc < 4:
                next_dirs = (d,)
            elif dc != 10:
                next_dirs = (((d + i) % 4) for i in (-1, 0, 1))
            else:
                next_dirs = (((d + i) % 4) for i in (-1, 1))
            for nd in next_dirs:
                q.append(((r + DIRS[nd][0], c + DIRS[nd][1]), heat_loss, nd, 1 if nd != d else dc+1))
        print(result)
        return result

    puzzle = Puzzle(year=YEAR, day=DAY)

    #for part in ("a", "b"):
    for part in ("b"):
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
