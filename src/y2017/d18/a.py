#!/usr/bin/python3.11
"""2017 day 18."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 18
PART = "a"


def main():
    """Part a."""
    data = tuple(lines(get_data(day=DAY, year=YEAR)))
    print(f"{data=}")

    # Bug: originally had this as a defaultdict, which meant that unpack() always
    # returned 0 for integers
    registers = {i: 0 for i in [chr(ord("a") + j) for j in range(26)]}
    ic = 0
    last_sound = -1

    def unpack(x):
        return registers[x] if x in registers else int(x)

    result = 0
    while 0 <= ic < len(data):
        t = data[ic].split()
        if t[0] == "snd":
            last_sound = unpack(t[1])
        elif t[0] == "set":
            registers[t[1]] = unpack(t[2])
        elif t[0] == "add":
            registers[t[1]] += unpack(t[2])
        elif t[0] == "mul":
            registers[t[1]] *= unpack(t[2])
        elif t[0] == "mod":
            registers[t[1]] %= unpack(t[2])
        elif t[0] == "rcv" and unpack(t[1]) > 0:
            result = last_sound
            break
        # Bug: wrote down the wrong instruction name.
        elif t[0] == "jgz" and unpack(t[1]) > 0:
            ic += unpack(t[2])
            continue
        ic += 1

    print(f"{result=}")
    if result:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
