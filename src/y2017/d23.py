#!/usr/bin/python3.12
"""2017 day FIXME."""
from aocd.models import Puzzle
from collections import defaultdict
import math

YEAR = 2017
DAY = 23

REGISTERS = "abcdefgh"


def main():
    """Main."""

    def a(data):
        """Part a."""
        print(f"{data=}")
        registers = defaultdict(lambda: 0)
        lines = data.splitlines()
        ip = 0
        result = 0
        while ip < len(lines):
            op, l, r = lines[ip].split()
            if r in REGISTERS:
                r = registers[r]
            else:
                r = int(r)
            if op == "set":
                registers[l] = r
                ip += 1
            elif op == "sub":
                registers[l] -= r
                ip += 1
            elif op == "mul":
                registers[l] *= r
                result += 1
                ip += 1
            elif op == "jnz":
                if l in REGISTERS:
                    l = registers[l]
                else:
                    l = int(l)
                if l != 0:
                    ip += int(r)
                else:
                    ip += 1
        return result

    def b(data):
        """Part b."""
        print(f"{data=}")
        lines = data.splitlines()
        b = int(lines[0].split()[-1]) * int(lines[4].split()[-1]) - int(lines[5].split()[-1])
        c = b - int(lines[7].split()[-1])
        j = -int(lines[-2].split()[-1])

        def is_prime(n):
            if n % 2 == 0 and n > 2:
                return False
            return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        return len([x for x in range(b, c+j, j) if not is_prime(x)])

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
