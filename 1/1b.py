#!/usr/bin/python3.10
"""2022 day 1."""
from aocd import get_data, submit

YEAR = 2022
DAY = 1
PART = "b"

data = get_data(day=1, year=2022).split("\n")

print(f"{data=}")

elves = []
current = 0
for line in data:
    if not line:
        elves.append(current)
        current = 0
    else:
        current += int(line)
elves.append(current)
result = sum(sorted(elves, reverse=True)[0:3])

print(f"{result=}")
submit(result, part=PART, day=DAY, year=YEAR)
