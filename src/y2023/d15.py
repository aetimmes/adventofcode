#!/usr/bin/python3.12
"""2023 day 15."""
import re

from aocd.models import Puzzle

YEAR = 2023
DAY = 15


def hash(s):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result = result % 256
    return result


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        result = 0
        for step in data.strip().split(","):
            result += hash(step)
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        boxes = [[] for _ in range(256)]

        for step in data.strip().split(","):
            label = re.search(r"^[a-z]+", step).group()
            h = hash(label)
            if step[-1] == '-':
                for lens in boxes[h]:
                    if lens[0] == label:
                        boxes[h].remove(lens)
            else:  # if step [-2] == "=":
                fl = int(step.split("=")[1])
                found = False
                for lens in boxes[h]:
                    if lens[0] == label:
                        lens[1] = fl
                        found = True
                        break
                if not found:
                    boxes[h].append([label, fl])
        result = 0
        for i, box in enumerate(boxes):
            for j, lens in enumerate(box):
                result += (i+1)*(j+1)*lens[1]
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
