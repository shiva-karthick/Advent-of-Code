import sys
import math
from copy import deepcopy
from collections import defaultdict, deque

infile = sys.argv[1] if len(
    sys.argv) > 1 else 'AOC_2022\Day-21-Monkey-Math\input_.txt'
data = open(infile).read().strip()
lines = [x for x in data.split('\n')]

dict_ = {}


def f(name, h):
    words = dict_[name]
    if name == 'humn' and h >= 0:
        return h

    try:
        return int(words[0])
    except:
        assert len(words) == 3
        e1 = f(words[0], h)
        e2 = f(words[2], h)
        if words[1] == '+':
            return e1+e2
        elif words[1] == '*':
            return e1*e2
        elif words[1] == '-':
            return e1-e2
        elif words[1] == '/':
            return e1/e2
        else:
            assert False, expr


for line in lines:
    words = line.split()
    name = words[0][:-1]
    expr = line.split(':')[1]
    dict_[name] = expr.split()

print(int(f('root', -1)))

p1 = dict_['root'][0]
p2 = dict_['root'][2]

if f(p2, 0) != f(p2, 1):
    p1, p2 = p2, p1
assert f(p1, 0) != f(p1, 1)
assert f(p2, 0) == f(p2, 1)
target = f(p2, 0)

lo = 0
hi = int(1e20)
while lo < hi:
    mid = (lo+hi)//2
    score = target - f(p1, mid)
    if score < 0:
        lo = mid
    elif score == 0:
        print(mid)
        break
    else:
        hi = mid
