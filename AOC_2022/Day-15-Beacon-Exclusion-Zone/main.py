import re
import sys
import math
from copy import deepcopy
from collections import defaultdict, deque

infile = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
data = open(r'C:\\Users\\shank\\Desktop\\Advent-of-Code\\AOC_2022\\Day-15-Beacon-Exclusion-Zone\\input.txt').read().strip()
lines = [x for x in data.split('\n')]

S = set()
B = set()

# parse the input to collect the data and store into sets
for line in lines:
    words = line.split()
    sx, sy = words[2], words[3]  # sensor x, y position
    bx, by = words[8], words[9]  # beacon x, y position
    sx = int(sx[2:-1])  # typecast into int
    sy = int(sy[2:-1])  # typecast into int
    bx = int(bx[2:-1])  # typecast into int
    by = int(by[2:])  # typecast into int
    d = abs(sx-bx) + abs(sy-by)  # get the manhattan distance
    # Sensor coordinates and the manhattan distance and between beacons
    S.add((sx, sy, d))
    B.add((bx, by))  # beacons


def valid(x, y, S):
    for (sx, sy, d) in S:
        dxy = abs(x-sx)+abs(y-sy)
        if dxy <= d:
            return False  # beacon cannot be here
    return True


result_1 = 0
for x in range(-int(1e7), int(1e7)):  # Go through all possible x coordinates
    y = int(2e6)
    # y = int(10) # used only for test_input.txt
    if not valid(x, y, S) and (x, y) not in B:
        result_1 += 1
print(result_1)

n_checked = 0
# If there is only one possible position for another beacon, it *must* be distance d+1 from some beacon
# If not, we could find an adjacent position that is possible.
found_p2 = False
for (sx, sy, d) in S:
    # check all points that are d+1 away from (sx,sy)
    for dx in range(d+2):
        dy = (d+1)-dx
        for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            n_checked += 1
            x = sx+(dx*signx)
            y = sy+(dy*signy)
            if not(0 <= x <= 4000000 and 0 <= y <= 4000000):
                continue
            assert abs(x-sx)+abs(y-sy) == d+1
            if valid(x, y, S) and (not found_p2):
                print(x*4000000 + y)
                found_p2 = True
# print(n_checked, 4*sum_d) # these are approximately equal


def all_numbers(s): return [int(d) for d in re.findall("(-?\d+)", s)]
def md(p, q): return abs(p[0]-q[0])+abs(p[1]-q[1])


data_ = [all_numbers(line) for line in data.split("\n")]
radius = {(a, b): md((a, b), (c, d)) for (a, b, c, d) in data_}
scanners = radius.keys()

acoeffs, bcoeffs = set(), set()

for ((x, y), r) in radius.items():
    # gradient is 1
    acoeffs.add(y-x+r+1)
    acoeffs.add(y-x-r-1)

    # gradient is -1
    bcoeffs.add(x+y+r+1)
    bcoeffs.add(x+y-r-1)

bound = 4_000_000
for a in acoeffs:
    for b in bcoeffs:
        p = ((b-a)//2, (a+b)//2)
        if all(0 < c < bound for c in p):
            if all(md(p, t) > radius[t] for t in scanners):
                print(4_000_000*p[0]+p[1])
