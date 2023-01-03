#!/usr/bin/python3.11
"""2017 day 18."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 18
PART = "b"


def main():
    """Part b."""
    data = tuple(lines(get_data(day=DAY, year=YEAR)))
    print(f"{data=}")

    registers = [
        {i: 0 for i in [chr(ord("a") + j) for j in range(26)]} for _ in range(2)
    ]
    for n in [0, 1]:
        registers[n]["p"] = n

    ics = [0, 0]
    queues = [[], []]
    states = [0, 0]

    # Bug: forgot to add [i] to `if x in registers`, causing int("p") to get evaled
    def unpack(x):
        return registers[i][x] if x in registers[i] else int(x)

    result = 0
    while not all(state for state in states):
        for i, ic in enumerate(ics):
            if 0 <= ic < len(data):
                t = data[ic].split()
                if t[0] == "snd":
                    queues[i].append(unpack(t[1]))
                    if i == 1:
                        result += 1
                elif t[0] == "set":
                    registers[i][t[1]] = unpack(t[2])
                elif t[0] == "add":
                    registers[i][t[1]] += unpack(t[2])
                elif t[0] == "mul":
                    registers[i][t[1]] *= unpack(t[2])
                elif t[0] == "mod":
                    registers[i][t[1]] %= unpack(t[2])
                elif t[0] == "rcv":
                    if not queues[i - 1]:
                        states[i] = 1
                        continue
                    registers[i][t[1]] = queues[i - 1].pop(0)
                    states[i] = 0
                elif t[0] == "jgz" and unpack(t[1]) > 0:
                    ics[i] += unpack(t[2])
                    continue
                ics[i] += 1
            else:
                states[i] = 2

    print(f"{result=}")
    if result:
        submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
