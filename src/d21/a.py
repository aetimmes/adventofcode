#!/usr/bin/python3.10
"""2022 day 21."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 21
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    nums = {}
    ops = {}
    for line in data:
        (ls, rs) = line.split(": ")
        if len(rs.split()) == 1:
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

    result = nums["root"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
