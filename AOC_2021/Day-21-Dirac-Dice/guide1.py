import collections
import itertools
import functools

counts = collections.Counter(sum(roll)
                             for roll in itertools.product((1, 2, 3), repeat=3))

print(counts)

ZERO, ONE = 0, 1


@functools.cache
def count(p1turn, p1, p2, s1, s2):  # p1turn = bool, p1/2 = positions, s1/2 = scores
    # Base cases
    if s1 >= 21:
        return ONE
    if s2 >= 21:
        return ZERO
    total = 0
    # Recursive case
    for roll, times in counts.items():
        p = p1 if p1turn else p2
        p = (p + roll) % 10
        if p1turn:
            total += times * count(not p1turn, p, p2, s1 + p + 1, s2)
        else:
            total += times * count(not p1turn, p1, p, s1, s2 + p + 1)
    # returns total number of times p1 won (or p2 if ONE and ZERO swapped)
    return total


p1, p2 = 6, 2
p1 -= 1
p2 -= 1
a1 = count(True, p1, p2, 0, 0)
ONE, ZERO = ZERO, ONE
a2 = count(True, p1, p2, 0, 0)
print(max(a1, a2))
