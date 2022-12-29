#!/usr/bin/python3.11
"""2016 day 23."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 23
PART = "b"

DATA = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    #data = lines(DATA)
    print(f"{data=}")

    result = 0

    registers = {i: 0 for i in "abcd"}
    registers["a"] = 12
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
                ic += registers[tokens[2]] if tokens[2] in registers else int(tokens[2])
            else:
                ic += 1
        elif tokens[0] == "tgl":
            index = registers[tokens[1]]
            if 0 <= index + ic < len(data):
                tgl_tokens = data[index + ic].split()
                if tgl_tokens[0] == "inc":
                    tgl_tokens[0] = "dec"
                elif tgl_tokens[0] == "jnz":
                    tgl_tokens[0] = "cpy"
                elif len(tgl_tokens) == 2:
                    tgl_tokens[0] = "inc"
                elif len(tgl_tokens) == 3:
                    tgl_tokens[0] = "jnz"

                data[index + ic] = " ".join(tgl_tokens)
            ic += 1

    result = registers["a"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
