#!/usr/bin/python3.10
"""2022 day 3."""
from aocd import get_data, submit

YEAR = 2022
DAY = 3
PART = "a"

data = get_data(day=DAY, year=YEAR).split("\n")
print(f"{data=}")

m: dict[str, int] = {}
for i in range(0, 26):
    m[chr(ord('a')+i)] = i + 1
    m[chr(ord('A')+i)] = i + 27

result = 0
for line in data:
    t1 = set(line[:len(line)//2])
    for c in line[len(line)//2:]:
        if c in t1:
            result += m[c]
            break
print(f"{result=}")
submit(result, part=PART, day=DAY, year=YEAR)
