from itertools import product, permutations
from collections import deque


def psub(p1, p2):
    # Subtract 2 points
    return p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2]


def padd(p1, p2):
    # Add 2 poinsts
    return p1[0]+p2[0], p1[1]+p2[1], p1[2]+p2[2]


def rotate(s, a, b, c, i, j, k):
    # rotate a point
    return (a*s[i], b*s[j], c*s[k])


def rotations(scan):
    # 24 orientations
    return {r: {rotate(s, *r)
                for s in scan} for r in orientations}


def scanit(scan, rebased0):
    rotations_ = rotations(scan).items()
    print(f'\nrotations_ = {rotations_}')
    for rot, rot_scan in rotations(scan).items():
        rebased = {p1: {psub(p1, p2) for p2 in rot_scan} for p1 in rot_scan}
        for p1, p2 in [(p1, p2) for p1 in rebased0 for p2 in rebased]:
            if len(rebased0[p1] & rebased[p2]) > 11:
                return p1, p2, rot


def make_absolute(scanners):
    scanner_locs = {(0, 0, 0)}
    task_list = deque([*enumerate(scanners[1:], start=1)])
    while task_list:
        i, scan = task_list.popleft()
        rebased0 = {p1: {psub(p1, p2)
                         for p2 in scanners[0]} for p1 in scanners[0]}
        result = scanit(scan, rebased0)
        if result == None:
            task_list.append((i, scanners[i]))
            continue
        p1, p2, rot = result
        scanner_locs.add(padd((0, 0, 0), psub(p1, p2)))  # Calculate the offset
        for s in scan:
            x = rotate(s, *rot)
            x = padd(x, psub(p1, p2))  # Add the offset
            if x not in rebased0[p1]:
                scanners[0].add(x)
    return len(scanners[0]), scanner_locs


orientations = [(1, 1, 1, 0, 1, 2), (1, 1, 1, 1, 2, 0), (1, 1, 1, 2, 0, 1), (1, 1, -1, 2, 1, 0), (1, 1, -1, 1, 0, 2), (1, 1, -1, 0, 2, 1), (1, -1, -1, 0, 1, 2), (1, -1, -1, 1, 2, 0), (1, -1, -1, 2, 0, 1), (1, -1, 1, 2, 1, 0), (1, -1, 1, 1, 0, 2), (1, -1, 1, 0, 2, 1),
                (-1, 1, -1, 0, 1, 2), (-1, 1, -1, 1, 2, 0), (-1, 1, -1, 2, 0, 1), (-1, 1, 1, 2, 1, 0), (-1, 1, 1, 1, 0, 2), (-1, 1, 1, 0, 2, 1), (-1, -1, 1, 0, 1, 2), (-1, -1, 1, 1, 2, 0), (-1, -1, 1, 2, 0, 1), (-1, -1, -1, 2, 1, 0), (-1, -1, -1, 1, 0, 2), (-1, -1, -1, 0, 2, 1)]

filename = 'AOC_2021\Day-19\sample.txt'

tmp = [{eval(line) for line in scanner.splitlines(
) if '--' not in line} for scanner in open(filename).read().split('\n\n')]

# tmp is a list containing sets(many tuples of 3 values)
print(type(tmp[0]))

beacons, scanner_locs = make_absolute(tmp)

print('part1:', beacons)


def mhd(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2])


print('part2', max(mhd(a, b) for a, b in permutations(scanner_locs, 2)))
