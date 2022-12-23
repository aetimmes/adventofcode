#!/usr/bin/python3.10
"""2022 day 7."""
from aocd import get_data, submit

YEAR = 2022
DAY = 7
PART = "a"


class Dir:
    """Directory."""

    def __init__(self, path: str):
        """Initialize."""
        self.path = path
        self.subdirs: list[Dir] = []
        self.size = 0

    def total_size(self) -> int:
        """Get total size of this and subdirs."""
        return self.size + sum(sd.total_size() for sd in self.subdirs)


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    dirs: dict[str, Dir] = {}
    cwd = []

    data.pop(0)  # We're at the root node
    dirs[""] = Dir("")
    while data:
        tokens = data.pop(0).split()
        if tokens[1] == "cd":
            if tokens[2] == "..":
                cwd.pop(-1)
            else:
                cwd.append(tokens[2])
        elif tokens[1] == "ls":
            continue
        elif tokens[0] == "dir":
            dirs["/".join(cwd + [tokens[1]])] = Dir("/".join(cwd + [tokens[1]]))
            dirs["/".join(cwd)].subdirs.append(dirs["/".join(cwd + [tokens[1]])])
        else:
            dirs["/".join(cwd)].size += int(tokens[0])

    result = 0
    for d in dirs.values():
        current = d.total_size()
        if current <= 100000:
            result += current

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
