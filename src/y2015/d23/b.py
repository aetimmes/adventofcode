#!/usr/bin/python3.11
"""2015 day 23."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 23
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    registers = {"a": 1, "b": 0}

    ic = 0
    print(f"{len(data)=}")
    while ic < len(data):
        current = data[ic]
        print(f"{ic=}, {current=}, {registers=}")
        tokens = current.split()
        if tokens[0] == "inc":
            registers[tokens[1]] += 1
            ic += 1
        elif tokens[0] == "hlf":
            registers[tokens[1]] //= 2
            ic += 1
        elif tokens[0] == "tpl":
            registers[tokens[1]] *= 3
            ic += 1
        elif tokens[0] == "jmp":
            ic += int(tokens[1])
        elif tokens[0] == "jio":
            if registers[tokens[1][0]] == 1:
                ic += int(tokens[2])
            else:
                ic += 1
        elif tokens[0] == "jie":
            if registers[tokens[1][0]] % 2 == 0:
                ic += int(tokens[2])
            else:
                ic += 1
        else:
            raise Exception("Parser failure")

    result = registers["b"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
