#!/usr/bin/python3.11
"""2015 day 22."""
import copy
import sys

from aocd import get_data, submit
from aocd.transforms import lines
from numpy import array

YEAR = 2015
DAY = 22
PART = "b"

(
    BOSS_HP,
    BOSS_DAMAGE,
    CURRENT_HP,
    CURRENT_MANA,
    MANA_SPENT,
    CURRENT_ARMOR,
    SHIELD_DURATION,
    POISON_DURATION,
    RECHARGE_DURATION,
) = (i for i in range(9))


def process_effects(state):
    """Process effects."""
    (
        boss_hp,
        boss_damage,
        current_hp,
        current_mana,
        mana_spent,
        current_armor,
        shield_duration,
        poison_duration,
        recharge_duration,
    ) = state

    if recharge_duration > 0:
        current_mana += 101
        recharge_duration -= 1
    if poison_duration > 0:
        boss_hp -= 3
        poison_duration -= 1
    if shield_duration > 0:
        current_armor = 7
        shield_duration -= 1
    else:
        current_armor = 0

    return array(
        [
            boss_hp,
            boss_damage,
            current_hp,
            current_mana,
            mana_spent,
            current_armor,
            shield_duration,
            poison_duration,
            recharge_duration,
        ]
    )


def process_attack(state):
    """Boss attacks."""
    (
        boss_hp,
        boss_damage,
        current_hp,
        current_mana,
        mana_spent,
        current_armor,
        shield_duration,
        poison_duration,
        recharge_duration,
    ) = state

    current_hp -= max(1, boss_damage - current_armor)

    return array(
        [
            boss_hp,
            boss_damage,
            current_hp,
            current_mana,
            mana_spent,
            current_armor,
            shield_duration,
            poison_duration,
            recharge_duration,
        ]
    )


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    temp = [int(line.split()[-1]) for line in data]
    (boss_hp, boss_damage) = temp
    initial = (
        array(
            [
                boss_hp,  # boss hp
                boss_damage,  # boss damage
                50,  # current_hp
                500,  # current_mana
                0,  # mana_spent
                0,  # current_armor
                0,  # shield duration
                0,  # poison duration
                0,  # recharge duration
            ]
        ),
        tuple(),
    )

    spells = [
        array([-4, 0, 0, -53, 53, 0, 0, 0, 0]),  # mm
        array([-2, 0, 2, -73, 73, 0, 0, 0, 0]),  # drain
        array([0, 0, 0, -113, 113, 0, 6, 0, 0]),  # shield
        array([0, 0, 0, -173, 173, 0, 0, 6, 0]),  # poison
        array([0, 0, 0, -229, 229, 0, 0, 0, 5]),  # recharge
    ]

    hard_mode = array([0, 0, -1, 0, 0, 0, 0, 0, 0])

    result = sys.maxsize
    winning_history = None
    q = [copy.deepcopy(initial)]
    while q:
        (current, history) = q.pop()
        current = current + hard_mode
        if current[CURRENT_HP] <= 0:
            continue
        current = process_effects(current)
        if current[BOSS_HP] <= 0:
            if current[MANA_SPENT] < result:
                result = current[MANA_SPENT]
                winning_history = history
            continue
        for i, spell in enumerate(spells):
            castable = True
            if current[CURRENT_MANA] < spell[MANA_SPENT]:
                castable = False
            for j in range(3):
                if (spell[SHIELD_DURATION + j] > 0) and (
                    current[SHIELD_DURATION + j] > 0
                ):
                    castable = False
            if not castable:
                continue
            new = current + spell
            new = process_effects(new)
            if new[BOSS_HP] <= 0:
                if new[MANA_SPENT] < result:
                    result = min(result, new[MANA_SPENT])
                    winning_history = history + (i,)
                continue
            new = process_attack(new)
            if (
                new[CURRENT_HP] <= 0
                or new[CURRENT_MANA] < 0
                or new[MANA_SPENT] >= result
            ):
                continue
            q.append((new, history + (i,)))

    print(f"{result=}")
    print(f"{winning_history=}")
    submit(int(result), part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
