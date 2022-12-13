#!/usr/bin/python3.10
"""2022 day 13."""
import bisect
import copy
import json

from aocd import get_data, submit

YEAR = 2022
DAY = 13
PART = "b"


class Packet:
    """Packet representation."""

    def __init__(self, val):
        """Initialize."""
        self.val = val

    def __le__(self, other):
        """Le override."""
        return Packet.cmp(self.val, other.val) in [0, 1]

    def __ge__(self, other):
        """Ge override."""
        return Packet.cmp(self.val, other.val) in [0, -1]

    def __lt__(self, other):
        """Lt override."""
        return Packet.cmp(self.val, other.val) == 1

    def __gt__(self, other):
        """Gt override."""
        return Packet.cmp(self.val, other.val) == -1

    def __eq__(self, other):
        """Eq override."""
        return Packet.cmp(self.val, other.val) == 0

    @staticmethod
    def cmp(x, y) -> int:
        """Compare two Packets, potentially recursively."""
        a = copy.deepcopy(x)
        b = copy.deepcopy(y)
        if isinstance(a, int):
            if isinstance(b, int):
                if a == b:
                    return 0
                elif a < b:
                    return 1
                else:
                    return -1
            else:
                return Packet.cmp([a], b)
        else:
            if isinstance(b, int):
                return Packet.cmp(a, [b])
            else:
                while a and b:
                    rc = Packet.cmp(a.pop(0), b.pop(0))
                    if rc != 0:
                        return rc
                if a:
                    return -1
                elif not a and not b:
                    return 0
                else:
                    return 1


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split("\n\n")
    print(f"{data=}")

    packets = []
    for chunk in data:
        (l, r) = [Packet(json.loads(s)) for s in chunk.split("\n")]
        packets.append(l)
        packets.append(r)

    packets.sort()

    a_i = bisect.bisect_left(packets, Packet([[2]]))
    bisect.insort_left(packets, Packet([[2]]))
    b_i = bisect.bisect_left(packets, Packet([[6]]))

    result = (a_i + 1) * (b_i + 1)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
