#!/usr/bin/python3.12
"""2017 day 25."""
from aocd.models import Puzzle
from collections import defaultdict

YEAR = 2017
DAY = 25

DIRECTIONS = {
    "left.": -1,
    "right.": 1
}

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        chunks = data.split("\n\n")
        steps = int(chunks[0].splitlines()[1].split()[-2])

        states = {}
        for chunk in chunks[1:]:
            lines = chunk.splitlines()
            state = {}
            name = lines[0][-2]
            state[0] = (
                int(lines[2].split()[-1][0]),     # write value
                DIRECTIONS[lines[3].split()[-1]], # direction
                lines[4][-2]                      # next state
            )
            state[1] = (
                int(lines[6].split()[-1][0]),     # write value
                DIRECTIONS[lines[7].split()[-1]], # direction
                lines[8][-2]                      # next state
            )
            states[name] = state

        state = "A"
        tape = defaultdict(lambda: 0)
        position = 0
        for _ in range(steps):
            directives = states[state][tape[position]]
            tape[position] = directives[0]
            position += directives[1]
            state = directives[2]
        return sum(tape.values())

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
