#!/usr/bin/python3.12
"""2023 day 24."""
from aocd.models import Puzzle
from z3 import Solver, Int, Real, sat
from itertools import combinations
from multiprocessing import Pool

YEAR = 2023
DAY = 24

MIN=200000000000000
MAX=400000000000000

def intersect(s0, s1):
    t0 = Real('t0')
    t1 = Real('t1')
    x = Real('x')
    y = Real('y')
    s = Solver()
    s.add(t0 > 0)
    s.add(t1 > 0)
    s.add(x == s0[0][0] + t0 * s0[1][0])
    s.add(x == s1[0][0] + t1 * s1[1][0])
    s.add(y == s0[0][1] + t0 * s0[1][1])
    s.add(y == s1[0][1] + t1 * s1[1][1])
    s.add(MIN <= x)
    s.add(x <= MAX)
    s.add(MIN <= y)
    s.add(y <= MAX)
    return s.check() == sat
        

def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        stones = []
        for line in data.splitlines():
            p,v = line.split(" @ ")
            x, y, z = list(map(int, p.split(", ")))
            dx, dy, dz = list(map(int, v.split(", ")))
            stones.append(((x,y,z),(dx,dy,dz)))
        
        p = Pool()
        results = [p.apply_async(intersect, c) for c in combinations(stones, 2)]
        
        return sum(r.get() for r in results)

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        rx = Int("rx")
        ry = Int("ry")
        rz = Int("rz")
        rdx = Int("rdx")
        rdy = Int("rdy")
        rdz = Int("rdz")
        z = Solver()
        ts = []
        for i, line in enumerate(data.splitlines()):
            p,v = line.split(" @ ")
            ix, iy, iz = list(map(int, p.split(", ")))
            dx, dy, dz = list(map(int, v.split(", ")))
            ts.append(Int(f"t{i}"))
            z.add(ts[0] > 0)
            z.add(ix + ts[i] * dx == rx + ts[i] * rdx)
            z.add(iy + ts[i] * dy == ry + ts[i] * rdy)
            z.add(iz + ts[i] * dz == rz + ts[i] * rdz)

        z.check()
        return (z.model()[rx].as_long() + z.model()[ry].as_long() + z.model()[rz].as_long())



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
