#!/usr/bin/python3.11
"""2015 day 21."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 21
PART = "b"

INPUT = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
None          0     0       0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
None          0     0       0
None          0     0       0
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"""


def player_wins(hp, damage, armor, boss_hp, boss_damage, boss_armor):
    """Determine if the player wins vs the boss."""
    while hp > 0 and boss_hp > 0:
        boss_hp -= max(damage - boss_armor, 1)
        if boss_hp <= 0:
            return True
        hp -= max(boss_damage - armor, 1)
    return False


def main():
    """Part b."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    boss_hp, boss_damage, boss_armor = map(int, [line.split()[-1] for line in data])

    (w, a, r) = INPUT.split("\n\n")
    weapons, armors, rings = [], [], []
    for line in w.splitlines()[1:]:
        weapons.append(tuple(map(int, line.split()[-3:])))
    for line in a.splitlines()[1:]:
        armors.append(tuple(map(int, line.split()[-3:])))
    for line in r.splitlines()[1:]:
        rings.append(tuple(map(int, line.split()[-3:])))

    result = 0

    for _, weapon in enumerate(weapons):
        for _, armor in enumerate(armors):
            for k, ring_a in enumerate(rings[:-1]):
                for _, ring_b in enumerate(rings[k + 1:]):
                    items = (weapon, armor, ring_a, ring_b)
                    cost = sum(item[0] for item in items)
                    if cost < result:
                        continue
                    damage = sum(item[1] for item in items)
                    armour = sum(item[2] for item in items)
                    if not player_wins(
                        100, damage, armour, boss_hp, boss_damage, boss_armor
                    ):
                        print(f"{items=}")
                        result = cost

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
