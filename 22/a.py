#!/usr/bin/python3.10
"""2022 day 22."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 22
PART = "a"

# down/right/clockwise is positive, deltas[0] is right
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
glyphs = [">", "v", "<", "^"]
turns = {"R": 1, "L": -1}


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)

    grid, instructions = data.split("\n\n")
    print(grid)
    grid = lines(grid)
    open_tiles = set()
    walls = set()

    max_r = len(grid)
    max_c = max(len(line) for line in grid)

    position: tuple[int, int] = (0, grid[0].index("."))
    facing: int = 0

    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == ".":
                open_tiles.add((r, c))
            elif char == "#":
                walls.add((r, c))

    result = 0

    current = ""
    for c in instructions:
        if c in ["L", "R"]:
            position = process_steps(
                open_tiles, walls, max_r, max_c, position, facing, current
            )
            facing = process_facing(facing, c)
            current = ""
        else:
            current += c

    if current:
        position = process_steps(
            open_tiles, walls, max_r, max_c, position, facing, current
        )

    result = ((position[0] + 1) * 1000) + ((position[1] + 1) * 4) + facing
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def process_steps(open_tiles, walls, max_r, max_c, position, facing, current):
    """Take a walk on a monkey forcefield."""
    steps = int(current)
    for _ in range(steps):
        temp = (
            (position[0] + deltas[facing][0]) % max_r,
            (position[1] + deltas[facing][1]) % max_c,
        )
        while temp not in open_tiles and temp not in walls:
            temp = (
                (temp[0] + deltas[facing][0]) % max_r,
                (temp[1] + deltas[facing][1]) % max_c,
            )
        if temp in open_tiles:
            position = temp
        if temp in walls:
            break
    return position


def process_facing(facing, c):
    """Turn! Turn! Turn! (To everything there is a facing)."""
    facing = (facing + turns[c]) % len(deltas)
    return facing


if __name__ == "__main__":
    main()
