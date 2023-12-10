#!/usr/bin/python3.12
"""2017 day 24."""
from aocd.models import Puzzle
import bisect
import functools

YEAR = 2017
DAY = 24


@functools.cache
def bt_a(components, selected, edge):
    result = sum(sum(components[i]) for i in selected)
    for i, c in enumerate(components):
        if i not in selected and edge in c:
            new_edge = c[(c.index(edge) + 1) % 2]
            result = max(result, bt_a(components, selected.union((i,)), new_edge))
    return result

@functools.cache
def bt_b(components, selected, edge):
    result = (len(selected), sum(sum(components[i]) for i in selected))
    for i, c in enumerate(components):
        if i not in selected and edge in c:
            new_edge = c[(c.index(edge) + 1) % 2]
            r = bt_b(components, selected.union((i,)), new_edge)
            if r[0] > result[0] or (r[0] == result[0] and r[1] > result[1]):
                result = r
    return result


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        components = (tuple(map(int, l.split("/"))) for l in data.splitlines())
        return bt_a((*components,), frozenset(), 0)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        components = (tuple(map(int, l.split("/"))) for l in data.splitlines())
        return bt_b((*components,), frozenset(), 0)[1]



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
