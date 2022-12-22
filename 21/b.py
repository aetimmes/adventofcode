#!/usr/bin/python3.10
"""2022 day 21."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 21
PART = "b"


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    nums = {}
    ops = {}
    root_sides = []
    for line in data:
        (ls, rs) = line.split(": ")
        if ls == "humn":
            # I peeked at the answer key to see if this worked:
            # We represent humn as a complex number in order to
            # isolate the variable algebraically without needing
            # to do weird parser stuff. Neat trick that I thought
            # about after seeing folks represent 2d grids with
            # complex numbers in earlier days.
            nums[ls] = 1j
        elif ls == "root":
            root_sides = [rs.split()[i] for i in [0, 2]]
        elif len(rs.split()) == 1:
            nums[ls] = int(rs)
        else:
            ops[ls] = rs
    while ops:
        pairs = list(ops.items())
        for k, v in pairs:
            tokens = v.split()
            if tokens[0] in nums and tokens[2] in nums:
                nums[k] = eval(  # pylint: disable=eval-used
                    f"{nums[tokens[0]]} {tokens[1]} {nums[tokens[2]]}"
                )
                del ops[k]

    a, b = (nums[root_sides[0]], nums[root_sides[1]])
    a, b = (b, a) if not a.imag else (a, b)
    result = round((b - a.real) / a.imag)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
