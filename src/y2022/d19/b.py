#!/usr/bin/python3.10
"""2022 day 19."""
from aocd import get_data, submit
from aocd.transforms import lines
from numpy import array

YEAR = 2022
DAY = 19
PART = "b"

TIME_LIMIT = 32


def sort_q(x):
    """Provide key for sort function."""
    return tuple(x[0][-i] + x[1][-i] for i in range(1, 5)) + ()


def main():
    """
    Part b.

    Methodology heavily inspired by
    https://old.reddit.com/r/adventofcode/comments/zpihwi/2022_day_19_solutions/j0tvzgz/
    """
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    blueprints = [
        [int(line.split()[j]) for j in [6, 12, 18, 21, 27, 30]] for line in data
    ]

    def sim_blueprint(bp):
        c_costs = (
            array([bp[0], 0, 0, 0]),
            array([bp[1], 0, 0, 0]),
            array([bp[2], bp[3], 0, 0]),
            array([bp[4], 0, bp[5], 0]),
        )
        q = [(array([0, 0, 0, 0]), array([1, 0, 0, 0]))]  # resources, robots

        for _ in range(TIME_LIMIT):
            next_q = []
            for (c_resources, c_robots) in q:
                # loop through all the robots we could make
                next_q.append((c_resources + c_robots, c_robots + array([0, 0, 0, 0])))
                for robot_type in range(4):
                    if all(c_costs[robot_type] <= c_resources):
                        next_robots = array(
                            [
                                ((c_robots[i] + 1) if i == robot_type else c_robots[i])
                                for i in range(4)
                            ]
                        )
                        next_q.append(
                            (c_resources + c_robots - c_costs[robot_type], next_robots)
                        )

            temp = sorted(next_q, key=sort_q)[-10000:]
            q = temp
        return max(e[0][-1] for e in q)

    result = 1
    for i, blueprint in enumerate(blueprints[:3]):
        current = sim_blueprint(blueprint)
        print(f"Blueprint {i}: {current}, quality level: {(i+1)*current}")
        result *= current
    print(f"{result=}")
    submit(int(result), part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
