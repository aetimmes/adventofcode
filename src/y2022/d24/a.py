#!/usr/bin/python3.11
"""2022 day 24."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 24
PART = "a"

# grid in r,c, top-left 0,0
DIRS = {">": 0, "v": 1, "<": 2, "^": 3}
DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]

DATA = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""


def bounds_check(r, c, mr, mc):
    """Don't wander out of the valley."""
    return (r, c) == (-1, 0) or (0 <= r < mr and 0 <= c < mc)


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    data.pop(0)
    data.pop()

    time = 0
    position = (-1, 0)
    blizzards = [set()]
    for r, line in enumerate(data):
        for c, char in enumerate(line[1:-1]):
            if char in DIRS:
                blizzards[time].add((r, c, DIRS[char]))

    max_rows = len(data)
    max_columns = len(data[0]) - 2
    goal_state = (max_rows, max_columns - 1)

    def gen_blizz(blizzards):
        current_blizzards = blizzards[-1]
        next_blizzards = set()
        for (r, c, d) in current_blizzards:
            next_r = (r + DELTAS[d][0]) % max_rows
            next_c = (c + DELTAS[d][1]) % max_columns
            next_blizzards.add((next_r, next_c, d))
        blizzards.append(next_blizzards)

    q = {position}
    result = 0
    while q:
        result += 1
        next_states = set()
        gen_blizz(blizzards)
        for (r, c) in q:
            for (dr, dc) in DELTAS:
                next_step = (r + dr, c + dc)
                if next_step == goal_state:
                    print(f"{result=}")
                    submit(result, part=PART, day=DAY, year=YEAR)
                    return
                if bounds_check(*next_step, max_rows, max_columns) and all(
                    (next_step[0], next_step[1], d) not in blizzards[result]
                    for d in range(4)
                ):
                    next_states.add(next_step)
        q = next_states


def print_grid(blizzards, mr, mc):
    """Print the grid if we need to debug."""
    result = ""
    for r in range(mr):
        for c in range(mc):
            dirs = []
            for d in range(4):
                if (r, c, d) in blizzards:
                    dirs.append(d)
            if len(dirs) == 0:
                result += "."
            elif len(dirs) == 1:
                result += ">v<^"[dirs[0]]
            else:
                result += str(len(dirs))
        result += "\n"
    print(result + "\n")


if __name__ == "__main__":
    main()
