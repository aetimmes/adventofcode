#!/usr/bin/python3.11
"""2022 day 17."""
from aocd import get_data, submit

YEAR = 2022
DAY = 17
PART = "a"

# bottom left is (0,0)
# grow bottom -> up, left -> right

flat = ((0, 0), (0, 1), (0, 2), (0, 3))
plus = ((1, 0), (1, 1), (0, 1), (2, 1), (1, 2))
el = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2))
eye = ((0, 0), (1, 0), (2, 0), (3, 0))
square = ((0, 0), (1, 0), (0, 1), (1, 1))

pieces = [flat, plus, el, eye, square]

num_pieces = len(pieces)

delta = {"<": -1, ">": 1}

def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    n_d = len(data)

    rocks = set()

    def bounds_check(r, c):
        return r >= 0 and c >= 0 and c < 7 and (r, c) not in rocks

    result = -1

    t = 0

    for i in range(2022):
        current_piece = [[r + result + 4, c + 2] for r, c in pieces[i % num_pieces]]
        while True:
            d = delta[data[t % n_d]]
            if all(bounds_check(r, c + d) for r, c in current_piece):
                for rock in current_piece:
                    rock[1] += d
            t += 1
            if all(bounds_check(r - 1, c) for r, c in current_piece):
                current_piece = [[r - 1, c] for (r, c) in current_piece]
            else:
                for (r, c) in current_piece:
                    rocks.add((r, c))
                result = max([result] + [r for r, _ in current_piece])
                break

    result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
