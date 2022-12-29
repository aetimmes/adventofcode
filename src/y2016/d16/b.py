#!/usr/bin/python3.11
"""2016 day 16."""
from aocd import get_data, submit

YEAR = 2016
DAY = 16
PART = "b"

bit_flip = {"0": "1", "1": "0"}

LENGTH = 35651584


def dragon_curve(a: str, length: int):
    while len(a) < length:
        b = reversed(a)
        b = "".join(bit_flip[bit] for bit in b)
        a = a + "0" + b
    return a


def checksum(a):
    while True:
        current = ""
        for i in range(0, len(a), 2):
            if a[i] == a[i + 1]:
                current += "1"
            else:
                current += "0"
        a = current
        if len(a) % 2 == 1:
            break
    return a


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    data = dragon_curve(data, LENGTH)[:LENGTH]
    result = checksum(data)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
