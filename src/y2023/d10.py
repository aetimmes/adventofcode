#!/usr/bin/python3.12
"""2023 day 10."""
from aocd.models import Puzzle
from collections import deque
import copy

YEAR = 2023
DAY = 10

# r, c
DELTAS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}

REPLACEMENTS = {
    "|": (".#.", ".#.", ".#."),
    "S": (".#.", ".#.", ".#."),
    "-": ("...", "###", "..."),
    "L": (".#.", ".##", "..."),
    "J": (".#.", "##.", "..."),
    "7": ("...", "##.", ".#."),
    "F": ("...", ".##", ".#."),
    ".": ("...", "...", "..."),
}


def boundscheck(x, y, mx, my):
    return x >= 0 and x < mx and y >= 0 and y < my


def expand_graph(lines, loop):
    ng = []
    for r, l in enumerate(lines):
        for c, e in enumerate(l):
            if (r, c) not in loop:
                e = "."
            for d, rl in enumerate(REPLACEMENTS[e]):
                if c == 0:
                    ng.append(rl)
                else:
                    ng[-3 + d] += rl
    return ng


def getstart(lines):
    for i, l in enumerate(lines):
        if "S" in l:
            return (
                i,
                l.index("S"),
            )


def getloop(lines):
    s = getstart(lines)
    seen = {s}
    # hardcoded for my input
    deck = deque([(s[0] + 1, s[1]), (s[0] - 1, s[1])])
    while deck:
        c = deck.popleft()
        if c in seen:
            continue
        seen.add(c)
        for d in DELTAS[lines[c[0]][c[1]]]:
            deck.append((c[0] + d[0], c[1] + d[1]))
    return seen


def main():
    """Main."""

    def a(data):
        """Part a."""
        print(f"{data=}")
        lines = data.split("\n")
        seen = getloop(lines)
        return len(seen) // 2

    def b(data):
        """Part b."""
        print(f"{data=}")
        lines = data.split("\n")
        loop = getloop(lines)
        graph = expand_graph(lines, loop)
        outside = set()
        deck = deque([(0, 0)])
        while deck:
            c = deck.pop()
            outside.add(c)
            for d in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = (c[0] + d[0], c[1] + d[1])
                if (
                    boundscheck(nr, nc, len(graph), len(graph))
                    and graph[nr][nc] != "#"
                    and (nr, nc) not in outside
                ):
                    deck.append((nr, nc))

        result = 0
        for r in range(1, len(graph), 3):
            for c in range(1, len(graph), 3):
                if (r, c) not in outside and graph[r][c] != "#":
                    result += 1

        return result

    puzzle = Puzzle(year=YEAR, day=DAY)
    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[part](ex.input_data)
                if (str(answer) != ex.getattr(f"answer_{part}")) and input(
                    f"Example data mismatch: {ex.getattr(f'answer_{part}')=}, {answer=}; submit anyways? [y/N]:"
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

        setattr(puzzle, f"answer_{part}", locals()[part](puzzle.input_data))


if __name__ == "__main__":
    main()
