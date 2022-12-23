#!/usr/bin/python3.10
"""2022 day 22."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 22
PART = "b"

# down/right/clockwise is positive, deltas[0] is right
deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
glyphs = [">", "v", "<", "^"]
turns = {"R": 1, "L": -1}

# r,c,facing
warps = {
    (0, 1, 3): (3, 0, 0),
    (0, 1, 2): (2, 0, 0),
    (0, 2, 0): (2, 1, 2),
    (0, 2, 1): (1, 1, 2),
    (0, 2, 3): (3, 0, 3),
    (1, 1, 0): (0, 2, 3),
    (1, 1, 2): (2, 0, 1),
    (2, 1, 0): (0, 2, 2),
    (2, 1, 1): (3, 0, 2),
    (2, 0, 2): (0, 1, 0),
    (2, 0, 3): (1, 1, 0),
    (3, 0, 0): (2, 1, 3),
    (3, 0, 1): (0, 2, 1),
    (3, 0, 2): (0, 1, 1),
}


def main():
    """Part b."""
    instructions, open_tiles, walls, r_section_length, c_section_length = parse_input()

    position: tuple[int, int] = (0, min(t[1] for t in open_tiles if t[0] == 0))
    facing: int = 0

    result = 0

    current = ""
    for c in instructions:
        if c in ["L", "R"]:
            position, facing = process_steps(
                open_tiles,
                walls,
                r_section_length,
                c_section_length,
                position,
                facing,
                current,
            )
            facing = process_facing(facing, c)
            current = ""
        else:
            current += c

    if current:
        position, facing = process_steps(
            open_tiles,
            walls,
            r_section_length,
            c_section_length,
            position,
            facing,
            current,
        )

    result = ((position[0] + 1) * 1000) + ((position[1] + 1) * 4) + facing
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def parse_input():
    """Spin a cube in our minds."""
    data = get_data(day=DAY, year=YEAR)

    grid, instructions = data.split("\n\n")
    print(grid)
    grid = lines(grid)
    open_tiles = set()
    walls = set()

    max_r = len(grid)
    max_c = max(len(line) for line in grid)
    r_section_length = max_r // 4
    c_section_length = max_c // 3

    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if char == ".":
                open_tiles.add((r, c))
            elif char == "#":
                walls.add((r, c))
    return instructions, open_tiles, walls, r_section_length, c_section_length


def process_steps(
    open_tiles, walls, r_section_length, c_section_length, position, facing, current
):
    """Take a walk on a cubular monkey forcefield."""
    steps = int(current)
    for _ in range(steps):
        temp_pos = (
            (position[0] + deltas[facing][0]),
            (position[1] + deltas[facing][1]),
        )
        temp_facing = facing
        if temp_pos not in open_tiles and temp_pos not in walls:
            temp_pos, temp_facing = process_warp(
                position, facing, r_section_length, c_section_length
            )
        if temp_pos in open_tiles:
            position = temp_pos
            facing = temp_facing
        if temp_pos in walls:
            break
    return position, facing


def process_warp(position, facing, r_section_length, c_section_length):
    """Take a leap of faith."""
    r, c = position
    r_section, c_section = get_sections(
        r - deltas[facing][0], c - deltas[facing][1], r_section_length, c_section_length
    )

    offset = None
    if facing == 0:
        offset = r % r_section_length
    elif facing == 1:
        offset = (-c - 1) % c_section_length
    elif facing == 2:
        offset = (-r - 1) % r_section_length
    elif facing == 3:
        offset = c % c_section_length
    r_section, c_section, facing = warps[(r_section, c_section, facing)]
    if facing == 0:
        r = r_section_length * (r_section) + offset
        c = c_section_length * (c_section)
    elif facing == 1:
        r = r_section_length * (r_section)
        c = c_section_length * (c_section + 1) - 1 - offset
    elif facing == 2:
        r = r_section_length * (r_section + 1) - 1 - offset
        c = c_section_length * (c_section + 1) - 1
    elif facing == 3:
        r = r_section_length * (r_section + 1) - 1
        c = c_section_length * (c_section) + offset
    return (r, c), facing


def get_sections(r, c, r_section_length, c_section_length):
    """Inspire some faith in a leap."""
    return ((r // r_section_length), (c // c_section_length))


def process_facing(facing, c):
    """Turn! Turn! Turn! (To everything there is a facing)."""
    facing = (facing + turns[c]) % len(deltas)
    return facing


if __name__ == "__main__":
    main()
