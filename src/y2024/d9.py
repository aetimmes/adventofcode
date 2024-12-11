#!/usr/bin/env python3
"""2024 day 9."""
from aocd.models import Puzzle

YEAR = 2024
DAY = 9


def main():
    """Main."""

    def a(data):
        """Part a."""
        print('\n'.join(data.splitlines()))
        nums = []
        dots = 0
        for i, c in enumerate(data.strip()):
            for _ in range(int(c)):
                if i % 2 == 0:
                    nums.append(i//2)
                else:
                    nums.append('.')
                    dots += 1
        l = 0
        while dots > 0:
            c = nums.pop()
            if c != '.':
                while nums[l] != '.':
                    l += 1
                nums[l] = c
            dots -= 1

        result = 0
        for i, n in enumerate(nums):
            result += i * n
        return result

    def b(data):
        """Part b."""
        print('\n'.join(data.splitlines()))
        files = []
        spaces = []
        pos = 0
        for i, c in enumerate(data.strip()):
            if i % 2 == 0:
                files.append((i//2, pos, int(c),))
            else:
                spaces.append((pos, int(c),))
            pos += int(c)

        n_files = []
        for (i, p, l) in files[::-1]:
            found = False
            for si, (sp, sl) in enumerate(spaces):
                if sp > p:
                    break
                if sl >= l:
                    n_files.append((i, sp, l))
                    spaces[si] = (sp+l, sl-l)
                    found = True
                    break
            if not found:
                n_files.append((i, p, l))

        return sum(i * sum(range(p, p+l)) for (i, p, l) in n_files)

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
