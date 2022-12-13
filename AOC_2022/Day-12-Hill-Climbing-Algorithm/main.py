import sys
import math
from copy import deepcopy
from collections import defaultdict, deque
from pprint import pprint

data = open('input.txt').read().strip()
lines = [x for x in data.split('\n')]

# BFS is used to find the shortest path on unweighted graphs.
# Start at some arbitrary node of a graphand explore the neighbournodes first.

maze = []
for line in lines:
    maze.append(line)
R = len(maze)
C = len(maze[0])

E = [[0 for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if maze[r][c] == 'S':
            E[r][c] = 1
        elif maze[r][c] == 'E':
            E[r][c] = 26
        else:
            E[r][c] = ord(maze[r][c]) - ord('a') + 1


def neighbours(i, j, diag=False):
    yield (i-1, j)
    yield (i+1, j)
    yield (i, j-1)
    yield (i, j+1)
    if diag:
        yield (i-1, j-1)
        yield (i-1, j+1)
        yield (i+1, j-1)
        yield (i+1, j+1)


def bfs(part):

    Q = deque()  # faster O(1) operations

    for r in range(R):
        for c in range(C):
            if (part == 1 and maze[r][c] == 'S') or (part == 2 and E[r][c] == 1):
                # find the starting coordinated in the maze
                Q.append(((r, c), 0))

    visited = set()

    while Q:  # FIFO deque
        (r, c), distance = Q.popleft()

        if (r, c) in visited:
            continue  # skip to the next iteration

        visited.add((r, c))

        # found!
        if maze[r][c] == 'E':
            return distance

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # check your neighbours
            rr = r+dr
            cc = c+dc
            # To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o.
            if (0 <= rr < R) and (0 <= cc < C) and (E[rr][cc] <= 1 + E[r][c]):
                Q.append(((rr, cc), distance + 1))


print(bfs(1))
print(bfs(2))
