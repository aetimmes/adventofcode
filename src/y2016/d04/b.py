#!/usr/bin/python3.11
"""2016 day 4."""
from collections import Counter

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 4
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = -1

    for line in data:
        ls, rs = line.split("[")
        ls = ls.split("-")
        sector_id = int(ls[-1])
        name = "".join(ls[:-1])
        c = Counter(name)
        mc = "".join(x[0] for x in sorted(c.items(), key=lambda x: (-x[1], x[0]))[:5])
        if rs[:-1] == mc:
            decrypted = ""
            name = " ".join(ls[:-1])
            for c in name:
                if c == " ":
                    decrypted += c
                    continue
                decrypted += chr((((ord(c) - ord("a") + sector_id) % 26) + ord("a")))
            if decrypted == "northpole object storage":
                result = sector_id
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
