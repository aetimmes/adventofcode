#!/usr/bin/env python3
"""2024 day 5."""
import functools
from collections import defaultdict
from aocd.models import Puzzle

YEAR = 2024
DAY = 5


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        rules, updates = data.split("\n\n")
        rm = defaultdict(set)
        for line in rules.splitlines():
            l,r = line.split("|")
            rm[int(l)].add(int(r))

        result = 0
        for u in updates.splitlines():
            good = True
            l = [int(x) for x in u.split(",")]
            for i, e in enumerate(l):
                for f in l[i+1:]:
                    if e in rm[f]:
                        good = False
            if good:
                print(f"works: {l}")
                result += l[len(l) // 2]
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        rules, updates = data.split("\n\n")
        rm = defaultdict(set)
        for line in rules.splitlines():
            l,r = line.split("|")
            rm[int(l)].add(int(r))

        def bfs(i, l):
            seen = set()
            stack = [i]
            while stack:
                c = stack.pop(0)
                seen.add(c)
                for e in rm[c]:
                    if e not in seen and e in l:
                        stack.append(e)
            return seen

        def reorder(l):
            m = []
            for e in l:
                m.append((len([x for x in bfs(e, set(l)) if x in l]), e))
            return sorted(m)[len(l)//2][1]

        result = 0
        for u in updates.splitlines():
            good = True
            l = [int(x) for x in u.split(",")]
            for i, e in enumerate(l):
                for f in l[i+1:]:
                    if e in rm[f]:
                        good = False
            if not good:
                result += reorder(l)
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
