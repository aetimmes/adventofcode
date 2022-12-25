#!/usr/bin/python3.10
"""2022 day 13."""
import bisect
from itertools import zip_longest
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
        return Packet.cmp(self.val, other.val) >= 0

    def __ge__(self, other):
        """Ge override."""
        return Packet.cmp(self.val, other.val) <= 0

    def __lt__(self, other):
        """Lt override."""
        return Packet.cmp(self.val, other.val) > 0

    def __gt__(self, other):
        """Gt override."""
        return Packet.cmp(self.val, other.val) < 0

    def __eq__(self, other):
        """Eq override."""
        return Packet.cmp(self.val, other.val) == 0

    @staticmethod
    def cmp(left, right) -> int:
        """Compare two Packets, potentially recursively."""
        rc = 0
        if isinstance(left, int):
            if isinstance(right, int):
                rc = right - left
            else:
                rc = Packet.cmp([left], right)
        else:
            if isinstance(right, int):
                rc = Packet.cmp(left, [right])
            else:
                for (l, r) in zip_longest(left, right, fillvalue=None):
                    rc = (l is None) - (r is None)
                    if rc == 0:
                        rc = Packet.cmp(l, r)
                    if rc != 0:
                        break
        return rc


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
