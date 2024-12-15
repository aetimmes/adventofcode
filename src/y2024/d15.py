#!/usr/bin/env python3
"""2024 day 15."""
from aocd.models import Puzzle

YEAR = 2024
DAY = 15

DS = {
    '<': -1j,
    '^': -1,
    '>': 1j,
    'v': 1
}

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        walls = set()
        blocks = set()
        data, steps = data.split("\n\n")
        for r, line in enumerate(data.splitlines()):
            for c, ch in enumerate(line.strip()):
                if ch == '#':
                    walls.add(r+c*1j)
                elif ch == 'O':
                    blocks.add(r+c*1j)
                elif ch == '@':
                    robot = r+c*1j
        for s in "".join(steps.splitlines()):
            if robot+DS[s] in walls:
                continue
            elif robot+DS[s] not in blocks:
                robot += DS[s]
            else:
                curr = robot+DS[s]
                while curr in blocks:
                    curr += DS[s]
                if curr in walls:
                    continue
                blocks.remove(robot+DS[s])
                blocks.add(curr)
                robot += DS[s]
        return int(sum(100*b.real + b.imag for b in blocks))




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
