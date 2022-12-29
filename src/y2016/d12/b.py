#!/usr/bin/python3.11
"""2016 day 12."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 12
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    registers = {i: 0 for i in "abcd"}
    registers["c"] = 1
    ic = 0
    while ic < len(data):
        current = data[ic]
        tokens = current.split()
        if tokens[0] == "cpy":
            if tokens[1] in registers:
                registers[tokens[2]] = registers[tokens[1]]
            else:
                registers[tokens[2]] = int(tokens[1])
            ic += 1
        elif tokens[0] == "inc":
            registers[tokens[1]] += 1
            ic += 1
        elif tokens[0] == "dec":
            registers[tokens[1]] -= 1
            ic += 1
        elif tokens[0] == "jnz":
            nz = registers[tokens[1]] if tokens[1] in registers else int(tokens[1])
            if nz != 0:
                ic += int(tokens[2])
            else:
                ic += 1

    result = registers["a"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
