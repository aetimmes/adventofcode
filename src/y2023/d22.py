#!/usr/bin/python3.12
"""2023 day 22."""
import copy
from aocd.models import Puzzle
from collections import defaultdict, deque

YEAR = 2023
DAY = 22


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        blocks = []
        for line in data.splitlines():
            l,r = line.split("~")
            blocks.append(
                list(map(int, l.split(","))) +
                list(map(int, r.split(",")))
            )
        blocks = sorted(blocks, key = lambda x: min(x[2], x[5]))
        
        occupied = {}
        load_bearing = defaultdict(set) 

        for i, b in enumerate(blocks):
            blocked = False
            while not blocked:
                for x in range(b[0], b[3]+1):
                    for y in range(b[1], b[4]+1):
                        z = min(b[2], b[5])
                        if (x,y,z-1) in occupied or z == 0:
                            blocked = True
                            if z != 0:
                                load_bearing[i].add(occupied[x,y,z-1])
                if not blocked:
                    b[2] -= 1
                    b[5] -= 1
            blocks[i] = b
            for x in range(b[0], b[3]+1):
                for y in range(b[1], b[4]+1):
                    for z in range(b[2], b[5]+1):
                        occupied[(x,y,z)] = i
        result = len(data.splitlines())
        for i in range(len(data.splitlines())):
            lb = False
            for k,v in load_bearing.items():
                if v == {i}:
                    lb = True
            if lb:
                result -= 1
        return result
        
        


    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        blocks = []
        for line in data.splitlines():
            l,r = line.split("~")
            blocks.append(
                list(map(int, l.split(","))) +
                list(map(int, r.split(",")))
            )
        blocks = sorted(blocks, key = lambda x: min(x[2], x[5]))
        
        occupied = {}
        load_bearing = defaultdict(set) 

        for i, b in enumerate(blocks):
            blocked = False
            while not blocked:
                for x in range(b[0], b[3]+1):
                    for y in range(b[1], b[4]+1):
                        z = min(b[2], b[5])
                        if (x,y,z-1) in occupied or z == 0:
                            blocked = True
                            if z != 0:
                                load_bearing[i].add(occupied[x,y,z-1])
                if not blocked:
                    b[2] -= 1
                    b[5] -= 1
            blocks[i] = b
            for x in range(b[0], b[3]+1):
                for y in range(b[1], b[4]+1):
                    for z in range(b[2], b[5]+1):
                        occupied[(x,y,z)] = i
        result = 0
        for i in range(len(data.splitlines())):
            lb = copy.deepcopy(load_bearing)
            d = deque()
            d.append(i)
            dropped = set()
            while d:
                c = d.pop()
                for k in lb:
                    if c in lb[k]:
                        lb[k].remove(c)
                        if lb[k] == set() and k not in dropped:
                            dropped.add(k)
                            d.append(k)
            result += len(dropped)
        return result
                        


    puzzle = Puzzle(year=YEAR, day=DAY)

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[part](ex.input_data)
                if (str(answer) != getattr(ex, f"answer_{part}")) and input(
                    f"Example data mismatch: {getattr(ex, f'answer_{part}')=}, {answer=}; submit anyways? [y/N]:"
                ).lower().strip() != "y":
                    exit()
            except Exception as e:
                print("Example data exception: %s" % str(e))
                if (
                    input("Example data exception; submit anyways? [y/N]:")
                    .lower()
                    .strip()
                    != "y"
                ):
                    raise
        answer = locals()[part](puzzle.input_data)
        print(f"{answer=}")
        setattr(puzzle, f"answer_{part}", answer)


if __name__ == "__main__":
    main()
