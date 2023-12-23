#!/usr/bin/python3.12
"""2023 day 19."""
from aocd.models import Puzzle

YEAR = 2023
DAY = 19


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
