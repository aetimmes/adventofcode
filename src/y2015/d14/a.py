#!/usr/bin/python3.11
"""2015 day 14."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 14
PART = "a"

TIME_LIMIT = 2503


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    reindeer = []

    for line in data:
        # speed, duration, rest
        reindeer.append(tuple(int(line.split()[i]) for i in [3, 6, -2]))

    result = 0
    for (speed, duration, rest) in reindeer:
        distance = 0
        running = 0
        resting = 0
        for _ in range(TIME_LIMIT):
            if running < duration:
                distance += speed
                running += 1
            else:
                resting += 1
                if resting == rest:
                    running = 0
                    resting = 0
        result = distance if distance > result else result

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
