#!/usr/bin/python3.11
"""2016 day 14."""
import hashlib

from aocd import get_data, submit

YEAR = 2016
DAY = 14
PART = "b"


def has_triple(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return ""


def has_quint(s, c):
    for i in range(len(s) - 4):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4] == c:
            return True
    return False


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    keys = []
    candidates = []
    index = 0
    while len(keys) < 64 or candidates:
        h = hashlib.md5((data + str(index)).encode("utf-8")).hexdigest()
        for _ in range(2016):
            h = hashlib.md5(h.encode("utf-8")).hexdigest()
        t = has_triple(h)
        if t != "":
            for c in candidates:
                if has_quint(h, c[1]):
                    keys.append(c)
            if len(keys) < 64:
                candidates.append((index, t))
        for c in tuple(candidates):
            if index - c[0] >= 1000:
                candidates.remove(c)
        index += 1

    result = sorted(keys)[63][0]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
