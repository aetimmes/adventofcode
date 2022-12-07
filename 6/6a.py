#!/usr/bin/python3.10
"""2022 day 6."""
from aocd import get_data, submit

YEAR = 2022
DAY = 6
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")[0]
    print(f"{data=}")
    print(f"{len(data)=}")

    m = {}
    for i in range(len(data)):
        if len(m.items())==4:
            result = i
            break
        m[data[i]] = m.get(data[i],0) + 1
        if i-4 >= 0:
            m[data[i-4]] -= 1
            if m[data[i-4]] == 0:
                del m[data[i-4]]
    

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
