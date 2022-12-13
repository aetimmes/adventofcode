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
        if isinstance(left, int):
            if isinstance(right, int):
                return right - left
            else:
                return Packet.cmp([left], right)
        else:
            if isinstance(right, int):
                return Packet.cmp(left, [right])
            else:
                for (l, r) in zip_longest(left, right, fillvalue=None):
                    if l is None and r is not None:
                        return 1
                    if l is not None and r is None:
                        return -1
                    rc = Packet.cmp(l, r)
                    if rc != 0:
                        return rc
                return 0


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
