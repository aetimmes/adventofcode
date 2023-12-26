#!/usr/bin/python3.12
"""2023 day 20."""
from collections import defaultdict, deque
from aocd.models import Puzzle

YEAR = 2023
DAY = 20

LO = 0
HI = 1


def main():
    """Main."""

    def a(data):
        """Part a."""
        print("\n".join(data.splitlines()))
        modules = {}  # name: type
        edges = {}  # input: output
        rev_edges = defaultdict(set)  # output: input
        states = {}  # (input, output): state
        for line in data.splitlines():
            ls, rs = line.split(" -> ")
            modules[ls[1:]] = ls[0]
            edges[ls[1:]] = rs.split(", ")
            states[ls[1:]] = LO
            for r in rs.split(", "):
                rev_edges[r].add(ls[1:])
                states[(ls[1:], r)] = LO

        pulses = [0, 0]
        q: deque[tuple[str, int, str]] = deque()
        for _ in range(1000):
            q.append(("button", 0, "roadcaster"))  # input, pulse, output
            while q:
                (i, p, o) = q.popleft()
                print(i, p, o)
                pulses[p] += 1
                if modules.get(o) == "%":
                    if p == LO:
                        states[o] += 1
                        states[o] %= 2
                        for e in edges[o]:
                            q.append((o, states[o], e))
                elif modules.get(o) == "&":
                    states[(i, o)] = p
                    np = LO if all(states[(e, o)] for e in rev_edges[o]) else HI
                    for e in edges[o]:
                        q.append((o, np, e))
                elif modules.get(o) == "b":
                    for e in edges[o]:
                        q.append((o, LO, e))

        return pulses[0] * pulses[1]

    def b(data):
        """Part b."""
        print("\n".join(data.splitlines()))

    puzzle = Puzzle(year=YEAR, day=DAY)

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[part](ex.input_data)
                if (str(answer) != getattr(ex, f"answer_{part}")) and input(
                    f"Example {part}{i} data mismatch: {getattr(ex, f'answer_{part}')=}, {answer=}; submit anyways? [y/N]:"
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
