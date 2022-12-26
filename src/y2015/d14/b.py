#!/usr/bin/python3.11
"""2015 day 14."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 14
PART = "b"

TIME_LIMIT = 2503


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    speeds = []
    running_durations = []
    resting_durations = []

    for line in data:
        # speed, duration, rest, score, running, resting, distance
        tokens = list(int(line.split()[i]) for i in [3, 6, -2])
        speeds.append(tokens[0])
        running_durations.append(tokens[1])
        resting_durations.append(tokens[2])

    scores = [0 for _ in speeds]
    running_times = [0 for _ in speeds]
    resting_times = [0 for _ in speeds]
    distances = [0 for _ in speeds]

    n = len(speeds)

    result = 0
    for _ in range(TIME_LIMIT):
        for i in range(n):
            if running_times[i] < running_durations[i]:
                distances[i] += speeds[i]
                running_times[i] += 1
            else:
                resting_times[i] += 1
                if resting_times[i] == resting_durations[i]:
                    resting_times[i] = 0
                    running_times[i] = 0

        leaders = [i for i, v in enumerate(distances) if v == max(distances)]
        for d in leaders:
            scores[d] += 1
    result = max(scores)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
