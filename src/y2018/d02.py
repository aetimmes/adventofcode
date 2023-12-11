#!/usr/bin/python3.12
"""2018 day 2."""
from aocd.models import Puzzle
from collections import Counter

YEAR = 2018
DAY = 2


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        twos = 0
        threes = 0
        for line in data.splitlines():
            c = Counter(line)
            if 2 in c.values():
                twos += 1
            if 3 in c.values():
                threes += 1
        return twos * threes

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        # BUG: forgot that sets are references; can't just mult them
        seen = []
        for _ in range(len(data.splitlines()[0])):
            seen.append(set())
        for line in data.splitlines():
            for i in range(len(line)):
                c = line[:i] + line[i+1:]
                if c in seen[i]:
                    return c
                seen[i].add(c)

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
