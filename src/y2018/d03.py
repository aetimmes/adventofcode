#!/usr/bin/python3.12
"""2018 day 3."""
from aocd.models import Puzzle

YEAR = 2018
DAY = 3


def overlap(b1, b2):
    pass # TODO


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        seen = set()
        counted = set()
        for line in data.splitlines():
            tokens = line.split()
            sx, sy = (int(x) for x in tokens[2][:-1].split(","))
            dx, dy = (int(x) for x in tokens[-1].split("x"))
            for x in range(sx, sx+dx):
                for y in range(sy, sy+dy):
                    if (x, y) in seen:
                        counted.add((x, y))
                    seen.add((x, y))
        return len(counted)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        boxes = []
        for line in data.splitlines():
            tokens = line.split()
            sx, sy = (int(x) for x in tokens[2][:-1].split(","))
            dx, dy = (int(x) for x in tokens[-1].split("x"))
            boxes.append((sx,sy),(dx,dy))
        for i, b1 in enumerate(boxes):
            valid = True
            for j, b2 in enumerate(boxes):
                if not valid or (i == j):
                    continue
                

            if valid:
                return data.splitlines()[i].split()[0][1:]

        return len(counted)


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
