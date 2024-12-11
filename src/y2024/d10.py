#!/usr/bin/env python3
"""2024 day 10."""
from collections import deque
from aocd.models import Puzzle

YEAR = 2024
DAY = 10

DS = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def main():
    """Main."""

    def a(data):
        """Part a."""
        print("\n".join(data.splitlines()))
        m = {x: set() for x in range(10)}
        for r, line in enumerate(data.splitlines()):
            for c, char in enumerate(line):
                m[int(char)].add((r, c,))

        result = 0
        for r, c in m[0]:
            seen = set()
            stack = deque()
            stack.append((r, c, 0,))
            while stack:
                (r, c, n) = stack.popleft()
                seen.add((r, c, n))
                for dr, dc in DS:
                    if (r + dr, c + dc) in m.get(n + 1, {}):
                        stack.append((r + dr, c + dc, n + 1))
            result += len([s for s in seen if s[2] == 9])
        return result

    def b(data):
        """Part b."""
        print("\n".join(data.splitlines()))
        m = {x: set() for x in range(10)}
        for r, line in enumerate(data.splitlines()):
            for c, char in enumerate(line):
                m[int(char)].add((r, c,))

        result = 0
        for r, c in m[0]:
            stack = deque()
            stack.append((r, c, 0,))
            while stack:
                (r, c, n) = stack.pop()
                if n == 9:
                    result+=1
                    continue
                for dr, dc in DS:
                    if (r + dr, c + dc) in m.get(n + 1, {}):
                        stack.append((r + dr, c + dc, n + 1))
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
