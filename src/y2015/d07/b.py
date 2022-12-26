#!/usr/bin/python3.11
"""2015 day 7."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 7
PART = "b"

LIMIT = 2**16


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    circuits = calculate(data, {})
    temp = circuits["a"]
    circuits = calculate(data, {"b": temp})

    result = circuits["a"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def calculate(data, circuits):
    """Attempt operations in sequence until we perform all of them."""
    q = data
    while q:
        next_ = []
        for line in q:
            ls, rs = line.split(" -> ")
            ls = ls.split()
            if len(ls) == 1:  # assignment
                if rs in circuits:
                    continue  # part b carryover
                if ls[0].isnumeric():
                    print(line)
                    circuits[rs] = int(ls[0]) % LIMIT
                    print(f"{circuits[rs]=}")
                elif ls[0] in circuits:
                    print(line)
                    circuits[rs] = circuits[ls[0]]
                    print(f"{circuits[ls[0]]=}, {circuits[rs]=}")
                else:
                    next_.append(line)
                continue
            if len(ls) == 2:  # not
                if ls[1] not in circuits:
                    next_.append(line)
                else:
                    print(line)
                    circuits[rs] = ~circuits[ls[1]] % LIMIT
                    print(f"{circuits[ls[1]]=}, {circuits[rs]=}")
                continue
            if (ls[0] not in circuits and not ls[0].isnumeric()) or (
                ls[2] not in circuits and not ls[2].isnumeric()
            ):
                next_.append(line)
                continue
            if ls[1] == "AND":
                if ls[0].isnumeric():
                    print(line)
                    # BUG - rs = 1 & N does not mean rs = N.
                    circuits[rs] = int(ls[0]) & circuits[ls[2]] % LIMIT
                    print(f"{ls[0]=}, {circuits[ls[2]]=}, {circuits[rs]=}")
                else:
                    print(line)
                    circuits[rs] = (circuits[ls[0]] & circuits[ls[2]]) % LIMIT
                    print(f"{circuits[ls[0]]=}, {circuits[ls[2]]=}, {circuits[rs]=}")
            elif ls[1] == "OR":
                print(line)
                circuits[rs] = (circuits[ls[0]] | circuits[ls[2]]) % LIMIT
                print(f"{circuits[ls[0]]=}, {circuits[ls[2]]=}, {circuits[rs]=}")
            elif ls[1] == "LSHIFT":
                print(line)
                circuits[rs] = (circuits[ls[0]] << int(ls[2])) % LIMIT
                print(f"{circuits[ls[0]]=}, {ls[2]=}, {circuits[rs]=}")
            elif ls[1] == "RSHIFT":
                print(line)
                circuits[rs] = (circuits[ls[0]] >> int(ls[2])) % LIMIT
                print(f"{circuits[ls[0]]=}, {ls[2]=}, {circuits[rs]=}")
        q = next_
    return circuits


if __name__ == "__main__":
    main()
