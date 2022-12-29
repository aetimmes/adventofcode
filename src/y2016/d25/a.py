#!/usr/bin/python3.11
"""2016 day 25."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 25
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    registers = {i: 0 for i in "abcd"}
    done = False
    while not done:
        result += 1
        registers["a"] = result
        target = 0
        states = [set(), set()]
        ic = 0
        while ic < len(data) and not done:
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
                    ic += (
                        registers[tokens[2]]
                        if tokens[2] in registers
                        else int(tokens[2])
                    )
                else:
                    ic += 1
            elif tokens[0] == "out":
                if registers[tokens[1]] != target:
                    break
                state = (registers["a"], registers["b"], registers["c"], registers["d"])
                if state in states[target]:
                    done = True
                    break
                states[target].add(state)
                target += 1
                target %= 2
                ic += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
