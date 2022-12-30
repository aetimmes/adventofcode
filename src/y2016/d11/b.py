#!/usr/bin/python3.11
"""2016 day 11."""
import itertools

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 11
PART = "b"


def is_legal(pairs):
    """Check if a state is legal."""
    for gen, chip in pairs:
        if chip == gen:
            continue
        if any(chip == g for g, _ in pairs):
            return False
    return True


def main():
    """
    Part b.

    Rewritten after taking a look at the spoiler threads. I did a whole bunch of work
    in the initial version to try avoid doing tuple addition that ended up borking my
    efficiency, even though I came up with the necessary insight (pairs are
    indistinguishable so states with different combos in the same positions should be
    pruned) when writing the first version.

    The additional pruning insight I had (once everything's on floor N, we never need to
    bring things back down to N-1 again) didn't really give a whole lot of speedup. The
    insight I didn't have until I looked at the spoiler thread was that if you can move
    two items up or one item down, you don't need to look at states moving one item up
    or two items down, respectively. The floor N pruning didn't actually result in any
    speedup; the +2/-1 pruning cut the runtime from 33s to <5s.
    """
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    # format is: elevator, (gen, chip)
    initial: tuple[int, tuple[tuple[int, int], ...]] = (
        0,
        ((0, 0), (0, 0), (0, 0), (1, 2), (1, 2), (1, 2), (1, 2)),
    )
    goal: tuple[int, tuple[tuple[int, int], ...]] = (
        3,
        tuple((3, 3) for _ in initial[1]),
    )

    result = -1
    i = 0
    q, seen = set(), set()
    q.add(initial)
    seen.add(initial)
    done = False
    while q and not done:
        i += 1
        next_q = set()
        while q:
            current = q.pop()
            if current == goal:
                result = i - 1
                done = True
                break
            ele_pos, pairs = current
            two_up, one_down = False, False
            for floor_delta, n_items in ((1, 2), (-1, 1), (1, 1), (-1, 2)):
                if two_up and (floor_delta, n_items) == (1, 1):
                    continue
                if one_down and (floor_delta, n_items) == (-1, 2):
                    continue
                new_ele_pos = ele_pos + floor_delta
                if not 0 <= new_ele_pos < 4:
                    continue
                if floor_delta == -1 and not any(
                    i in p for p in pairs for i in range(new_ele_pos + 1)
                ):
                    continue
                indices = (
                    (x, y)
                    for x in range(len(pairs))
                    for y in range(2)
                    if pairs[x][y] == ele_pos
                )
                candidates = set()
                for combo in itertools.combinations(indices, n_items):
                    candidate = tuple(
                        tuple(
                            pairs[x][y] + floor_delta
                            if (x, y) in combo
                            else pairs[x][y]
                            for y in range(2)
                        )
                        for x in range(len(pairs))
                    )
                    if is_legal(candidate) and (new_ele_pos, candidate) not in seen:
                        candidates.add(tuple(sorted(candidate)))
                for candidate in candidates:
                    if (floor_delta, n_items) == (1, 2):
                        two_up = True
                    if (floor_delta, n_items) == (-1, 1):
                        one_down = True
                    seen.add((new_ele_pos, candidate))
                    next_q.add((new_ele_pos, candidate))
        q = next_q
        print(f"{i=}, {len(q)=}")

    print(f"{result=}")
    if result > 0:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
