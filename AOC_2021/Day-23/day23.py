'''
1.  
    Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room.
    (That is , once any amphipod starts moving,
    any other amphipods currently in the hallway are locked in place
    and will not move again until they can move fully into a room.)

    can someone explain this, i think this is where im going wrong but im not sure
    does it mean that amphipods cant move from one position in the hallway to another

    yes
    you can only move room -> room, room -> hallway, hallway -> room
    you cannot move hallway -> hallway

    basically, each amphipod can only make up to 2 moves, ever
    out to the hall -> to the final place it needs to be
    it can't do anything else

    i always move room->hall and hall->room
    simplifies it

    each pod can only ever make at most 2 moves.
    one out of the room to the hall, one from the hall to he room in their final spot
    nothing else

2.  
    @lru_cache(maxsize=None)
    def solve(grid):
        if all(in_correct_room(pod) for pod in grid.pods):
            return 0

        lowest = float('inf')
        for i, pod in enumerate(grid.pods):
            char, (row, col) = pod
            for (nrow, ncol) in grid.available_spots_for(pod):
                step_cost = (abs(nrow-row) + abs(ncol-col)) * COST[char]

                grid.pods[i] = (char, (nrow, ncol))
                rec_cost = solve(grid)
                grid.pods[i] = (char, (row, col))

                if rec_cost + step_cost < lowest:
                    lowest = rec_cost + step_cost
        return lowest
    simple backtracking really

3.  
    dijkstra = a* but heuristic 0

4.  
    modular arithmetic is hard, i don't blame people
    i only know because i have been burned too often
    I found just putting input() right when the function is called and printing the grid super helpful
'''
# @Author : Mustafa
# I took this code to read and understand the problem, all rights to the author,
# his solutions are very understandbale to a layman like me :)

from common import *
from functools import lru_cache

with open('AOC_2021\Day-23\input.txt') as f:
    lines = f.read().split('\n')

COLS = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

pods = []
for i, line in enumerate(lines[1:-1]):
    for j, char in enumerate(line[1:-1]):
        if char in "ABCD":
            pods.append((char, (i, j)))


def in_room(pod):
    char, (row, col) = pod  # char, (row, col)
    return row > 0


def in_correct_room(pod):
    char, (row, col) = pod  # unpack the values
    return row > 0 and COLS[char] == col


class Grid:
    def __init__(self, pods, N):  # why is N = 2 ?
        self.pods = pods
        self.N = N

    def __hash__(self):
        return hash((tuple(self.pods), self.N))

    def __eq__(self, other):
        return self.pods == other.pods

    def __repr__(pods, N=2):
        grid = [list("╭―――――――――――╮"),
                list("│...........│"),
                list("╰―╮.│.│.│.╭―╯"),
                list("  │.│.│.│.│"),
                list("  │.│.│.│.│"),
                list("  │.│.│.│.│"),
                list("  ╰―┴―┴―┴―╯")]

        for char, (row, col) in pods:
            grid[row+1][col+1] = char

        grid = grid[:N+2]+grid[-1:]
        return "\n".join("".join(row) for row in grid)

    def available_spots_for(self, start):
        positions = {pos: c for c, pos in self.pods}
        visible = set()
        can_move = []

        def check_hall(col, offset):
            i = col
            while 0 <= i < 11 and (0, i) not in positions:
                if i not in (2, 4, 6, 8):
                    can_move.append((0, i))
                visible.add((0, i))
                i += offset

        char, (row, col) = start  # unpack the values

        if in_room(start):
            if in_correct_room(start):
                if row == self.N:
                    return []

                others = [
                    c for c, (ro, co) in self.pods if co == col and ro > row]
                assert len(others) > 0

                # Everything below me is the same amphipod, I'm done.
                if all(c == char for c in others):
                    return []

            # Trapped if there's something above me
            others = [c for c, (ro, co) in self.pods if co ==
                      col and 0 < ro < row]
            if len(others) > 0:
                return []

            check_hall(col+1, 1)
            check_hall(col-1, -1)
            return can_move
        else:
            check_hall(col+1, 1)
            check_hall(col-1, -1)
            dest_col = COLS[char]

            # Can't access the column to the room, no moves.
            if (0, dest_col) not in visible:
                return []

            # Don't go back in if there's other chars
            others = [c for c, (ro, co) in self.pods if co ==
                      dest_col and ro > row]
            if not all(c == char for c in others):
                return []

            # Elements in room are same, add myself
            return [(self.N - len(others), dest_col)]


@lru_cache(maxsize=None)
def solve(grid):
    # Base Case
    if all(in_correct_room(pod) for pod in grid.pods):
        return 0

    lowest = float('inf')
    for i, pod in enumerate(grid.pods):
        char, (row, col) = pod  # unpack the values
        for (nrow, ncol) in grid.available_spots_for(pod):
            step_cost = (abs(nrow-row) + abs(ncol-col)) * COST[char]

            grid.pods[i] = (char, (nrow, ncol))
            rec_cost = solve(grid)
            grid.pods[i] = (char, (row, col))

            if rec_cost + step_cost < lowest:
                lowest = rec_cost + step_cost
    return lowest


def part1():
    return solve(Grid(deepcopy(pods), 2))


def part2():
    cur_pods = deepcopy(pods)
    for i, pod in enumerate(cur_pods):
        char, (row, col) = pod
        if row == 2:
            cur_pods[i] = (char, (4, col))
    cur_pods += [('D', (2, 2)), ('C', (2, 4)), ('B', (2, 6)), ('A', (2, 8))]
    cur_pods += [('D', (3, 2)), ('B', (3, 4)), ('A', (3, 6)), ('C', (3, 8))]
    return solve(Grid(cur_pods, 4))


print("Part 1:", part1())
print(solve.cache_info())

print("Part 2:", part2())
print(solve.cache_info())
