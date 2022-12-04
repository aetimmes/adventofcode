#!/usr/bin/python3.10
"""2022 day TODO: FIXME."""
from aocd import get_data, submit

YEAR = 2022
DAY = 4
PART = "a"

data = get_data(day=DAY, year=YEAR).split("\n")
print(f"{data=}")

result = 0
for line in data:
    tokens = [t.split('-') for t in line.split(",")]
    le = int(tokens[0][0]) - int(tokens[1][0])
    ri = int(tokens[1][1]) - int(tokens[0][1])
    if (le <= 0 and ri <= 0) or (le >= 0 and ri >= 0):
        result += 1
print(f"{result=}")
submit(result, part=PART, day=DAY, year=YEAR)
