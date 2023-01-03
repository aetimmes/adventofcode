#!/usr/bin/python3.11
"""2017 day 20."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 20
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    positions = {}
    velocities = []
    accelerations = []
    for i, line in enumerate(data):
        p, v, a = line.split(", ")
        positions[tuple(map(int, p[3:-1].split(",")))] = i
        velocities.append(list(map(int, v[3:-1].split(","))))
        accelerations.append(list(map(int, a[3:-1].split(","))))

    for t in range(1000):
        if t % 1000 == 0:
            print(f"{t=}")
            print(f"{len(positions)=}")

        next_ = {}
        to_remove = set()
        for p, i in positions.items():
            for j in range(3):
                velocities[i][j] += accelerations[i][j]
            current = tuple(p[k] + velocities[i][k] for k in range(3))
            if current in next_:
                to_remove.add(current)
            next_[(current)] = i
        for r in to_remove:
            del next_[r]
        positions = next_

    result = len(positions)
    print(f"{result=}")
    if result >= 0:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
