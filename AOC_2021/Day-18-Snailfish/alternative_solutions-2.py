from functools import reduce
from math import ceil, floor


def add_leftmost(t, n):
    if isinstance(t, int):
        return t + n
    l, r = t  # here t is a list
    return [add_leftmost(l, n), r]


def add_rightmost(t, n):
    if isinstance(t, int):
        return t + n
    l, r = t
    return [l, add_rightmost(r, n)]


def explode(t, depth=0):
    if isinstance(t, int):
        return False, None, None, t
    l, r = t
    if depth >= 4 and isinstance(l, int) and isinstance(r, int):
        return True, l, r, 0
    z, a, b, l = explode(l, depth=depth+1)
    if z:
        if b is not None:
            r = add_leftmost(r, b)
        return z, a, None, [l, r]
    z, c, d, r = explode(r, depth=depth+1)
    if z:
        if c is not None:
            l = add_rightmost(l, c)
        return z, None, d, [l, r]
    return False, None, None, [l, r]


def split(t):
    if isinstance(t, int):
        if t >= 10:
            l, r = floor(t / 2), ceil(t / 2)
            return True, [l, r]
        return False, t
    l, r = t
    z, l = split(l)
    if z:
        return z, [l, r]
    z, r = split(r)
    if z:
        return z, [l, r]
    return False, [l, r]


def loop_process(t):
    while True:
        f = False
        while True:
            z, _, _, t = explode(t)
            if not z:
                break
            f = True
        z, t = split(t)
        if not f and not z:
            break
    return t


def plus(x, y):
    return loop_process([x, y])


def magnitude(t):
    if isinstance(t, int):
        return t
    l, r = t
    return 3 * magnitude(l) + 2 * magnitude(r)


with open('AOC_2021\Day-18-Snailfish\sample.txt') as f:
    exprs = list(map(eval, f))
    print(exprs)

print('Part 1:', magnitude(reduce(plus, exprs)))
print('Part 2:', max(magnitude(plus(a, b)) for i, a in enumerate(exprs)
      for j, b in enumerate(exprs) if i != j))
