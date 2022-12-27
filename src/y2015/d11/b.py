#!/usr/bin/python3.11
"""2015 day 11."""
from aocd import get_data, submit

YEAR = 2015
DAY = 11
PART = "b"


def increment(chars):
    """Increment the chars."""
    carry = 1
    for i, c in enumerate(chars):
        chars[i] = (c + carry) % 26
        if carry and chars[i] == 0:
            carry = 1
        else:
            carry = 0
    return chars


def test_pw(chars):
    """Check password legality."""
    if any((ord(c) - ord("a")) in chars for c in "iol"):
        return False
    straight = False
    first_pair = None
    second_pair = False
    for i in range(len(chars)):  # pylint: disable=consider-using-enumerate
        if (
            not straight
            and i < len(chars) - 3
            and chars[i] == (chars[i + 1] + 1) == (chars[i + 2] + 2)
        ):
            straight = True
        if (not second_pair) and (i < (len(chars) - 1)) and (chars[i] == chars[i + 1]):
            if first_pair is None:
                first_pair = chars[i]
            elif first_pair != chars[i]:
                second_pair = True
    return straight and second_pair


def nums_to_string(chars):
    """Get string from nums."""
    return "".join([chr(ord("a") + c) for c in reversed(chars)])


def string_to_nums(string):
    """Get nums from string."""
    return [ord(c) - ord("a") for c in reversed(string)]


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    # data = "abcdefgh"
    print(f"{data=}")

    test_pw(string_to_nums("abcdffaa"))

    chars = increment(string_to_nums(data))

    while not test_pw(chars):
        chars = increment(chars)

    chars = increment(chars)
    while not test_pw(chars):
        chars = increment(chars)
    result = nums_to_string(chars)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
