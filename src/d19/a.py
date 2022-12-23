#!/usr/bin/python3.10
"""2022 day 19."""
from collections import defaultdict, deque
import sys
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 19
PART = "a"

DATA = """Blueprint 1: Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore.  Each clay robot costs 3 ore.  Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian."""

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

TIME_LIMIT = 24


def main():
    """Part a."""
    # data = lines(get_data(day=DAY, year=YEAR))
    data = lines(DATA)
    print(f"{data=}")

    result = 0

    blueprints = [[int(l.split()[j]) for j in [6, 12, 18, 21, 27, 30]] for l in data]

    def sim_blueprint(bp):
        max_geodes = 0
        costs = {
            ORE: {ORE: bp[0]},
            CLAY: {ORE: bp[1]},
            OBSIDIAN: {ORE: bp[2], CLAY: bp[3]},
            GEODE: {ORE: bp[4], OBSIDIAN: bp[4]},
        }
        time: int = 0
        c_robots: tuple[int, int, int, int] = (1, 0, 0, 0)
        c_resources: tuple[int, int, int, int] = (0, 0, 0, 0)

        q: deque[
            tuple[int, tuple[int, int, int, int], tuple[int, int, int, int]]
        ] = deque([(time, c_resources, c_robots)])

        fastest_states = defaultdict(int)
        i = 0
        while q:
            i += 1
            (c_time, c_resources, c_robots) = q.pop()
            compare_max = True
            # loop through all the robots we could make
            for robot_type in range(4):
                max_t = -1
                for cost_type in costs[robot_type]:
                    if c_robots[cost_type] != 0:
                        max_t = max(
                            max_t,
                            (costs[robot_type][cost_type] - c_resources[cost_type])
                            // c_robots[cost_type],
                        )
                    else:
                        max_t = sys.maxsize
                if c_time + max_t + 1 <= TIME_LIMIT:
                    compare_max = False
                    time = c_time + max_t + 1
                    resources = tuple(
                        c_resources[i]
                        + (c_robots[i] * (max_t + 1))
                        - costs[robot_type].get(i, 0)
                        for i in range(4)
                    )
                    robots = tuple(
                        r + 1 if i == robot_type else r for i, r in enumerate(c_robots)
                    )
                    if fastest_states.get((resources, robots), sys.maxsize) > time:
                        fastest_states[(resources, robots)] = time
                        q.append((time, resources, robots))
            if compare_max:
                total_geodes = c_resources[3] + c_robots[3] * (TIME_LIMIT - c_time)
                max_geodes = total_geodes if total_geodes > max_geodes else max_geodes
        return max_geodes

    for i, blueprint in enumerate(blueprints):
        result += (i + 1) * sim_blueprint(blueprint)
    print(f"{result=}")
    # submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
