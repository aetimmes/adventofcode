#!/usr/bin/python3.12
"""2023 day 25."""
import random
from aocd.models import Puzzle
import networkx as nx

YEAR = 2023
DAY = 25


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        g = nx.Graph()
        n_seen = set()
        e_seen = set()
        for line in data.splitlines():
            ls, rs = line.split(": ")
            for r in rs.split():
                g.add_node(ls)
                g.add_node(r)
                g.add_edge(ls, r, capacity=1)
        done = False
        while not done:
            x,y = random.choices(list(g.nodes), k=2)
            cut_value, partition = nx.minimum_cut(g,x,y)
            if cut_value == 3:
                done = True
                return len(partition[0]) * len(partition[1])
                

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
