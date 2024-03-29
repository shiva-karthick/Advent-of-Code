# Author:https://github.com/mustafaquraish/aoc-2021/blob/master/python/19.py
# @mustafaquraish
# Understandable solution
#


from common import *
from itertools import combinations
from functools import cache

with open('AOC_2021\Day-19\sample.txt') as f:
    text = f.read().strip()


def get_vec(line):
    return tuple(map(int, re.findall('-?\d+', line)))


data = [frozenset(map(get_vec, area.split('\n')[1:]))
        for area in text.split('\n\n')]


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


@cache
def pairwise_dists(lst):
    return {p: {sum((x-y)**2 for x, y in zip(p, q)) for q in lst} for p in lst}


def orient(pt, orientation):
    a, b, c = pt
    return (
        (+a, +b, +c), (+b, +c, +a), (+c, +a, +
                                     b), (+c, +b, -a), (+b, +a, -c), (+a, +c, -b),
        (+a, -b, -c), (+b, -c, -a), (+c, -a, -
                                     b), (+c, -b, +a), (+b, -a, +c), (+a, -c, +b),
        (-a, +b, -c), (-b, +c, -a), (-c, +a, -
                                     b), (-c, +b, +a), (-b, +a, +c), (-a, +c, +b),
        (-a, -b, +c), (-b, -c, +a), (-c, -a, +
                                     b), (-c, -b, -a), (-b, -a, -c), (-a, -c, -b)
    )[orientation]


def all_possible_orientations(pts):
    return ((i, {orient(x, i) for x in pts}) for i in range(24))


def enough_common_points(offs1, offs2):
    for x, xv in offs1.items():
        for y, yv in offs2.items():
            if len(xv & yv) >= 12:  # set operator
                return (x, y)


def do_scanners_match(scanner1, scanner2):
    dists1 = pairwise_dists(scanner1)
    dists2 = pairwise_dists(scanner2)
    if not (result := enough_common_points(dists1, dists2)):
        return False
    p1, p2 = result
    print(f'p1 = {p1}')
    print(f'p2 = {p2}')
    offs1 = set(sub(p1, q) for q in scanner1)
    offs2 = set(sub(p2, q) for q in scanner2)
    print(f'offs1 = {offs1}')
    print(f'offs2 = {offs2}')
    for ori, lst in all_possible_orientations(offs2):
        if len(offs1 & lst) >= 12:
            return sub(p1, orient(p2, ori)), ori


remaining = deepcopy(data)
beacons = remaining.pop(0)
locations = {(0, 0, 0)}

while remaining:
    for i, d in enumerate(remaining):
        if result := do_scanners_match(beacons, d):
            offset, ori = result
            locations.add(offset)
            beacons |= {add(orient(b, ori), offset) for b in d}
            remaining.pop(i)
            break

max_dist = max(
    sum(abs(x-y) for x, y in zip(a, b))
    for a, b in combinations(locations, 2)
)

print("Part 1:", len(beacons))
print("Part 2:", max_dist)
