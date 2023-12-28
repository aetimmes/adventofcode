#!/usr/bin/python3.12
"""2023 day 19."""
from collections import deque
import copy
from aocd.models import Puzzle

YEAR = 2023
DAY = 19


def isvalid(r):
    return all(1 <= r[i][0] <= r[i][1] <= 4000 for i in "xmas")


def main():
    """Main."""

    def part_a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        r, p = data.split("\n\n")
        rules = {}
        result = 0
        for line in r.splitlines():
            ls, rs = line.split("{")
            rules[ls] = rs[:-1].split(",")

        for part in p.splitlines():
            for c in part[1:-1].split(","):
                exec(f"global {c[0]}; {c}")
            rule = rules["in"]
            while rule != "done":
                for claus in rule:
                    if "<" in claus or ">" in claus:
                        (ls, rs) = claus.split(":")
                        if not eval(ls):
                            continue
                        elif rs not in "AR":
                            rule = rules[rs]
                            break
                        elif rs == "A":
                            result += (x+m+a+s)
                            rule = "done"
                            break
                        elif rs == "R":
                            rule = "done"
                            break
                        else:
                            print("PANIC")
                            raise
                    elif claus not in "AR":
                        rule = rules[claus]
                        break
                    elif claus == "A":
                        result += (x+m+a+s)
                        rule = "done"
                        break
                    elif claus == "R":
                        rule = "done"
                        break
                    else:
                        print("PANIC")
                        raise
        return result

    def part_b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        r, p = data.split("\n\n")
        rules = {}
        result = 0
        for line in r.splitlines():
            ls, rs = line.split("{")
            rules[ls] = rs[:-1].split(",")
        
        result = 0
        d = deque()
        solutions = list()
        d.append({"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000],"r":"in"})
        while d:
            c = d.popleft()
            if not isvalid(c):
                continue
            for claus in rules[c[r]].split(","):
                if claus == "A":
                    solutions.add(copy.deepcopy(c))
                    break
                elif claus == "R":
                    break
                elif "<" in claus:
                    ls, rs = claus.split(":")
                    ll, lr = ls.split("<")
                    nc = copy.deepcopy(c)
                    nc[ll][1] = min(nc[ll][1], int(lr))
                    if isvalid(nc):
                        if rs == "A":
                                solutions.add(nc)
                        elif rs != "R":
                            nc[r] = rs
                            d.append(nc)
                    c[ll][0] = max(c[ll][0], int(lr))
                elif ">" in claus:
                    ls, rs = claus.split(":")
                    ll, lr = ls.split("<")
                    nc = copy.deepcopy(c)
                    nc[ll][0] = max(nc[ll][0], int(lr))
                    if isvalid(nc):
                        if rs == "A":
                                solutions.add(nc)
                        elif rs != "R":
                            nc[r] = rs
                            d.append(nc)
                    c[ll][1] = min(c[ll][1], int(lr))
                else:
                    c[r] = claus
                    d.append(c)
        for s in solutions:
            r = 1
            for c in "xmas":
                r *= s[c] 
            result += r
        return result

                



    puzzle = Puzzle(year=YEAR, day=DAY)

    for part in ("a", "b"):
        for i, ex in enumerate(puzzle.examples):
            try:
                answer = locals()[f"part_{part}"](ex.input_data)
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
        answer = locals()[f"part_{part}"](puzzle.input_data)
        print(f"{answer=}")
        setattr(puzzle, f"answer_{part}", answer)


if __name__ == "__main__":
    main()
