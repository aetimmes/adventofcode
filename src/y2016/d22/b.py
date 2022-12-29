#!/usr/bin/python3.11
"""2016 day 22."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 22
PART = "b"

USED = 0
AVAIL = 1

deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def can_move(source, dest):
    return source[USED] != 0 and source != dest and source[USED] <= dest[AVAIL]


def move(source, dest):
    return (0, source[AVAIL] + source[USED]), (
        dest[USED] + source[USED],
        dest[AVAIL] - source[USED],
    )


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    nodes = {}
    for line in data[2:]:
        tokens = line.split()
        x, y = (int(t[1:]) for t in tokens[0].split("-")[1:])
        used = int(tokens[2][:-1])
        avail = int(tokens[3][:-1])
        nodes[(x, y)] = (used, avail)
    goal = (max(x for (x, _) in nodes), 0)

    empty = (-1, -1)
    for x in range(max(x for x, _ in nodes) + 1):
        current = ""
        for y in range(max(y for _, y in nodes) + 1):
            if (x, y) == goal:
                current += "G"
            elif nodes[(x, y)][USED] == 0:
                current += "_"
                empty = (x, y)
            elif nodes[(x, y)][USED] > 200:
                current += "#"
            else:
                current += "."
        print(current)

    print(f"{goal=}")
    print(f"{empty=}")

    # The map looks like:

    # *..........................
    # .......#...................
    # .......#...................
    # .......#............_......
    # .......#...................
    # .......#...................

    #               .
    #               .
    #               .

    # .......#...................
    # .......#...................
    # .......#...................
    # .......#...................
    # G......#...................

    # Path for goal is a straight line. Move count is the number of moves it takes to
    # get the goal and empty nodes adjacent to each other (sum of the x/y coords of the
    # empty node and the x coord of the goal) and then 5 * the number of remaining nodes
    # (the goal's x coord - 1 since we've swapped it once).

    result = empty[0] + empty[1] + goal[0] + 5 * (goal[0] - 1)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
