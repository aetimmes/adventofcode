#!/usr/bin/env python3
"""2024 day 2."""
from aocd.models import Puzzle

YEAR = 2024
DAY = 2


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        for line in data.splitlines():
            c = None
            asc = None
            safe = True
            for i in map(int, line.split()):
                if not c:
                    c = i
                    continue
                if asc == None:
                    asc = 1 if (i > c) else -1
                if not (0 < (i - c)*asc <= 3):
                    safe = False
                    break
                c = i

            if safe:
                result += 1
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        result = 0
        def is_safe(l):
            c = None
            asc = None
            safe = True

            for i in l:
                if not c:
                    c = i
                    continue
                if asc == None:
                    asc = 1 if (i > c) else -1
                if not (0 < (i - c)*asc <= 3):
                    safe = False
                    break
                c = i
            return safe

        for line in data.splitlines():
            orig = list(map(int, line.split()))
            safe = is_safe(orig)
            if not safe:
                for j in range(len(orig)):
                    curr = orig[:j] + orig[j+1:]
                    if is_safe(curr):
                        result += 1
                        break
            if safe:
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
