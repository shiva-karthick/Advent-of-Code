import sys
from decimal import Decimal
import math
from copy import deepcopy
from collections import defaultdict, deque

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

G = lines
R = len(G)
C = len(G[0])
# print(G,R,C)

r = 0
c = 0
while G[r][c] == '#':  # find the entry coordinate
    c += 1

# pre-compute where the obstacles are
BAD_CELLS = {}

for t in range((R - 2) * (
        C - 2) + 1):  # R - 2 because 2 walls on each side and C - 2 because 2 columns are on each side; + 1 because of python range function
    # count the number of time units taken
    BAD = set()  # Blizzards set
    for rr in range(R):  # go through the grid
        for cc in range(C):  # go through the grid
            if G[rr][cc] == '>':
                BAD.add((rr, 1 + ((cc - 1 + t) % (C - 2))))  # the % wrap around the wall >## then ##>
            elif G[rr][cc] == 'v':
                BAD.add((1 + ((rr - 1 + t) % (R - 2)), cc))
            elif G[rr][cc] == '<':
                BAD.add((rr, 1 + ((cc - 1 - t) % (C - 2))))
            elif G[rr][cc] == '^':
                BAD.add((1 + ((rr - 1 - t) % (R - 2)), cc))
                assert 0 <= (rr - 1 - t) % (R - 2) < R - 2
            if cc == c:
                assert G[rr][cc] != '^' and G[rr][cc] != 'v' # it should be a wall
            if cc == C - 2:
                assert G[rr][cc] != '^' and G[rr][cc] != 'v' # it should be a wall
    BAD_CELLS[t] = BAD  # dictionary [time_unit] = set of all blizzards at that current time

p1 = False
SEEN = set()
start = (r, c, 0, False, False)  # state: row, column, time_unit
queue = deque([start])

while queue:
    # === Standard BFS Stuff ===
    (r, c, t, got_end, got_start) = queue.popleft()
    if not (0 <= r < R and 0 <= c < C and G[r][c] != '#'):  # check for boundaries
        continue
    if r == R - 1 and got_end and got_start:  # stop if the end is reached
        print(t)
        break

    # part 2 stuff
    if r == R - 1 and (not p1):
        print(t)
        p1 = True
    if r == R - 1:
        got_end = True
    if r == 0 and got_end:
        got_start = True
    # t %= ((R-2)*(C-2))

    # === Standard BFS Stuff ===
    if (r, c, t, got_start, got_end) in SEEN:
        continue
    SEEN.add((r, c, t, got_start, got_end))

    BAD = BAD_CELLS[t + 1]  # get the current time set; potential bug source

    # consider all the 5 moves
    if (r, c) not in BAD:
        queue.append((r, c, t + 1, got_end, got_start))
    if (r + 1, c) not in BAD:
        queue.append((r + 1, c, t + 1, got_end, got_start))
    if (r - 1, c) not in BAD:
        queue.append((r - 1, c, t + 1, got_end, got_start))
    if (r, c + 1) not in BAD:
        queue.append((r, c + 1, t + 1, got_end, got_start))
    if (r, c - 1) not in BAD:
        queue.append((r, c - 1, t + 1, got_end, got_start))
