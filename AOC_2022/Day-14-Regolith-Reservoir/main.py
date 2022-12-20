import sys
import math
from copy import deepcopy
from collections import defaultdict, deque

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

R = set()

# Note down the positionsof the rocks
for line in lines:
    prev = None
    for point in line.split('->'):
        x, y = point.split(',')
        x, y = int(x), int(y)  # map(int, x)
        if prev is not None:
            dx = x-prev[0]
            dy = y-prev[1]
            len_ = max(abs(dx), abs(dy))
            for i in range(len_+1):
                xx = prev[0]+i*(1 if dx > 0 else (-1 if dx < 0 else 0))
                yy = prev[1]+i*(1 if dy > 0 else (-1 if dy < 0 else 0))
                R.add((xx, yy))
        prev = (x, y)

# two plus the highest y coordinate of any point in your scan.
floor = 2 + max(r[1] for r in R)
print(f'floor = {floor}')
# Why - 2000? ;assume the floor is an infinite horizontal line
lo_x = min(r[0] for r in R) - 2000
# Why + 2000? ;assume the floor is an infinite horizontal line
hi_x = max(r[0] for r in R) + 2000
for x in range(lo_x, hi_x):
    R.add((x, floor))

print(f'min([r[1] for r in R]) = {min([r[1] for r in R])}')

did_p1 = False
for t in range(1000000):
    rock = (500, 0)
    while True:
        # +1 because of 0 based indexing
        if rock[1]+1 >= floor and (not did_p1):
            did_p1 = True
            print(f'part 1 result = {t}')
        if (rock[0], rock[1]+1) not in R:  # sand falling down
            rock = (rock[0], rock[1]+1)
        elif (rock[0]-1, rock[1]+1) not in R:  # sand falling to the left
            rock = (rock[0]-1, rock[1]+1)
        elif (rock[0]+1, rock[1]+1) not in R:  # sand falling to the right
            rock = (rock[0]+1, rock[1]+1)
        else:
            break
    if rock == (500, 0):
        print(t+1)
        break
    R.add(rock)
