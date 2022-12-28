#!/usr/bin/python3.11
"""2016 day 7."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 7
PART = "b"


def supports_ssl(line):
    """Check an IP to see if it supports SSL."""
    outies = []
    innies = []
    while "[" in line:
        ls, line = line.split("[", 1)
        outies.append(ls)
        mid, line = line.split("]", 1)
        innies.append(mid)
    if line:
        outies.append(line)
    abas = []
    for o in outies:
        abas.extend(get_abas(o))
    babs = [aba[1] + aba[0] + aba[1] for aba in abas]
    return any((bab in innie for bab in babs for innie in innies))


def get_abas(s):
    """Return all ABAs in a string."""
    result = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            result.append(s[i:i + 3])
    return result


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    for line in data:
        if supports_ssl(line):
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
