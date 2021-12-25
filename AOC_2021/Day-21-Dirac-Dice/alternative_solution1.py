from common import *
from itertools import cycle, product
from functools import cache, lru_cache

with open('AOC_2021\Day-21-Dirac-Dice\input.txt') as f:
    text = f.read().strip()

_, a, _, b = get_all_ints(text)


def part1(a, b):
    sa, sb = 0, 0
    dice = iter(cycle(range(1, 101)))  # dice
    count = 0
    while sb < 1000:
        roll = next(dice) + next(dice) + next(dice)
        count += 3
        a = (a + roll) % 10
        a, sa, b, sb = b, sb, a, sa + a + 1
    return sa * count


@cache
def part2_1(a, b, sa=0, sb=0):
    if sb >= 21:
        return (0, 1)
    wa, wb = 0, 0
    weights = (1, 3, 6, 7, 6, 3, 1)
    for i in range(7):
        ta = (a + i + 3) % 10
        rb, ra = part2_1(b, ta, sb, sa + ta + 1)
        wa, wb = wa + ra * weights[i], wb + rb * weights[i]
    return (wa, wb)


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


# Code golf'ed part 2, 132 chars
P = cache(lambda a, b, A=0, B=0: 1j*(B > 20) or sum((-1j*P(b, (a+x+3) % 10, B,
          A+1+(a+x+3) % 10)*(1, 3, 6, 7, 6, 3, 1)[x]).conjugate()for x in range(7)))

print("Part 1:", part1(a-1, b-1))
print("Part 2:", max(part2_2(a, b, 0, 0)))

'''
well to me DP is using (cached) recursive subproblems to build up a solution to your full problem

So importing the caching is fine, and it reduces code complexity, and it's a bit faster than using your own. but (1) it's good to implement your own so that you understand what it's doing better, and (2) implementing your own gives you more flexibility as to what you key the cache off of.

You can compare using your own:
def playgame(pos_a, score_a, pos_b, score_b, cache={}):
    if (pos_a, score_a, pos_b, score_b) not in cache:
        #code here
        cache[pos_a, score_a, pos_b, score_b] = result
    return cache[pos_a, score_a, pos_b, score_b]

vs importing:
from functools import lru_cache
@lru_cache(maxsize=None)
def playgame(pos_a, score_a, pos_b, score_b, cache={}):
    #code here
    return result

Functionally the result will be the same here.
'''
