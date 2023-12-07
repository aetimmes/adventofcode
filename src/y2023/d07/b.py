#!/usr/bin/python3.11
"""2023 day 7b."""
from aocd import get_data, submit
from collections import Counter, defaultdict
from dataclasses import dataclass
import bisect
YEAR = 2023
DAY = 7
PART = "b"

CARDS = "J23456789TQKA"


@dataclass
class Hand:
    cards: str
    hand: list
    bid: int

    def __init__(self, line):
        self.cards = line
        h, b = line.split()
        self.bid = int(b)
        c = Counter([CARDS.index(i) for i in h])
        if "J" in self.cards:
            jokers = c.pop(CARDS.index("J"))
        else:
            jokers = 0
        hand = []
        for k, v in c.items():
            bisect.insort(hand, v)
        if hand:
            hand[-1] += jokers
        else:
            hand = [5]
        self.hand = hand

    def __lt__(self, other):
        # check hand ranks
        if self.hand != other.hand:
            for i in range(-1, -6, -1):
                if self.hand[i] != other.hand[i]:
                    return self.hand[i] < other.hand[i]
        # if hand ranks are tied, check card ranks
        for i in range(5):
            if CARDS.index(self.cards[i]) != CARDS.index(other.cards[i]):
                return CARDS.index(self.cards[i]) < CARDS.index(other.cards[i])


def main():
    """Part a."""
    lines = get_data(day=DAY, year=YEAR).split("\n")
    result = 0
    hands = []
    for line in lines:
        hand = Hand(line)
        bisect.insort(hands, hand)

    for i, hand in enumerate(hands):
        result += (i+1) * hand.bid
        print(i, hand.cards)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
