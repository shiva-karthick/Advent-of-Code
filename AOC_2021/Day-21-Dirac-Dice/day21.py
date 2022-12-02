from functools import lru_cache
from itertools import cycle, product
from common import *


@lru_cache
def part1():  # p1turn = bool, pos_1/2 = positions, sa/b = scores
    with open('AOC_2021\Day-21-Dirac-Dice\input.txt') as f:
        text = f.read().strip()

    pos_1, pos_2 = (int(s[-1]) for s in text.split('\n'))
    # p1turn = bool, p1/2 = positions, s1/2 = scores
    # Player 1 position is 6
    # Player 2 position is 2

    sa, sb = 0, 0
    dice = iter(cycle(range(1, 101)))
    count = 0

    while True:
        pos_1 = (pos_1 + (next(dice) + next(dice) + next(dice)) - 1) % 10 + 1
        pos_2 = (pos_2 + (next(dice) + next(dice) + next(dice)) - 1) % 10 + 1

        sa += pos_1
        sb += pos_2

        if sb >= 1000:
            print((sa - pos_1) * (count + 3))
            break
        elif sa >= 1000:
            print((sb - pos_2) * (count + 3))
            break
        count += 6

        print(f'sa = {sa}, sb = {sb}, count = {count}')


@lru_cache(maxsize=None)
def part2_2(a_posit, o_posit, a_score, o_score):
    A, O = 0, 0
    for roll in product(range(1, 4), repeat=3):
        posit = ((a_posit+sum(roll))-1) % 10+1
        score = a_score + posit
        o, a = (0, 1) if score >= 21 else part2_2(
            o_posit, posit, o_score, score)
        A, O = A+a, O+o
        print(f'A = {A}, O = {O}')
    return A, O


print("Part 1:", part1())
