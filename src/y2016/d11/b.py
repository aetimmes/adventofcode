#!/usr/bin/python3.11
"""2016 day 11."""
import itertools
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 11
PART = "b"

elements = [
    "promethium",
    "cobalt",
    "curium",
    "ruthenium",
    "plutonium",
]


def is_legal(floors):
    for floor in floors:
        gens = [i for i in floor if i < 10]
        chips = [i for i in floor if i >= 10]
        for c in chips:
            if gens and c // 10 not in gens:
                return False
    return True


def tuplize(floors):
    rep = [[-1, -1] for _ in range(7)]
    for i, floor in enumerate(floors):
        for e in floor:
            if e < 10:
                rep[e - 1][0] = i
            else:
                rep[(e // 10) - 1][1] = i
    return tuple(sorted(tuple(r) for r in rep))


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    initial: tuple[int, tuple[set[int], set[int], set[int], set[int]]] = (
        0,
        ({1, 10, 6, 7, 60, 70}, {2, 3, 4, 5}, {20, 30, 40, 50}, set()),
    )
    goal = (3, (set(), set(), set(), {1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 60, 70}))
    q = [initial]
    done = False
    result = -1
    seen = set()
    while not done and q:
        result += 1
        print(result)
        next_q = []
        while q:
            ele_pos, floors = q.pop()
            seen.add((ele_pos, tuplize(floors)))
            for num_items in (1, 2):
                for combo in itertools.combinations(floors[ele_pos], num_items):
                    for next_ele_pos in [
                        ele_pos + i for i in [1, -1] if 0 <= ele_pos + i < 4
                    ]:
                        new_floors = []
                        for f in range(0, 4):
                            if f == ele_pos:
                                new_floors.append(floors[f].difference(combo))
                            elif f == next_ele_pos:
                                new_floors.append(floors[f].union(set(combo)))
                            else:
                                new_floors.append(floors[f])
                        new_floors = tuple(new_floors)
                        next_state = (next_ele_pos, new_floors)
                        if (next_ele_pos, tuplize(new_floors)) in seen:
                            continue
                        if next_state == goal:
                            done = True
                        if is_legal(new_floors):
                            next_q.append(next_state)
        #q = next_q
        q = sorted(
           next_q,
           key=lambda x: (len(x[1][0]), len(x[1][1]), len(x[1][2]), len(x[1][3])),
        )[:1000000]  # setting this to 1k/10k wasn't permissive enough
        print(f"{len(q)=}")

    print(f"{result=}")
    if result > 0:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
