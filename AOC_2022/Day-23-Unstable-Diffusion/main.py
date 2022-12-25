from collections import defaultdict, deque

data = open('AOC_2022\Day-23-Unstable-Diffusion\input.txt').read()
lines = [x for x in data.split('\n')]

elves = set()
grid = lines
for row, column in enumerate(grid):
    for column_num, char in enumerate(column):
        if char == '#':  # add all the elves to a set
            elves.add((row, column_num))


def show(elves):
    r1 = min(row for (row, column) in elves)
    r2 = max(row for (row, column) in elves)
    c1 = min(column for (row, column) in elves)
    c2 = max(column for (row, column) in elves)
    for row in range(r1, r2+1):
        row = ''
        for column in range(c1, c2+1):
            row += ('#' if (row, column) in elves else '.')
        print(row)
    print('='*80)


dir_list = ['N', 'S', 'W', 'E']

for t in range(10000):
    any_moved = False
    # proposed_location[(row,column)] is the list of elves who want to move to (row,column)

    proposed_location = defaultdict(list)

    for (row, column) in elves:
        # if you don't have any neighbor, stay put and don't move
        has_neighbour = False
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr != 0 or dc != 0) and (row+dr, column+dc) in elves:
                    has_neighbour = True  # if has neighbour update the status
        if not has_neighbour:  # if no neighbour, continue
            continue

        moved = False
        for dir_ in dir_list:
            if dir_ == 'N' and (not moved) and (row-1, column) not in elves and (row-1, column-1) not in elves and (row-1, column+1) not in elves:
                proposed_location[(row-1, column)].append((row, column))
                moved = True
            elif dir_ == 'S' and (not moved) and (row+1, column) not in elves and (row+1, column-1) not in elves and (row+1, column+1) not in elves:
                proposed_location[(row+1, column)].append((row, column))
                moved = True
            elif dir_ == 'W' and (not moved) and (row, column-1) not in elves and (row-1, column-1) not in elves and (row+1, column-1) not in elves:
                proposed_location[(row, column-1)].append((row, column))
                moved = True
            elif dir_ == 'E' and (not moved) and (row, column+1) not in elves and (row-1, column+1) not in elves and (row+1, column+1) not in elves:
                proposed_location[(row, column+1)].append((row, column))
                moved = True

    dir_list = dir_list[1:]+[dir_list[0]]  # switch the directions list

    for k, vs in proposed_location.items():
        if len(vs) == 1:
            any_moved = True
            elves.discard(vs[0])
            elves.add(k)

    if not any_moved:
        print(t+1)
        break

    if t == 9:  # 10 times; part 1
        # get the bounding box
        r1 = min(row for (row, column) in elves)
        r2 = max(row for (row, column) in elves)
        c1 = min(column for (row, column) in elves)
        c2 = max(column for (row, column) in elves)
        ans = 0
        for row in range(r1, r2+1):
            for column in range(c1, c2+1):
                if (row, column) not in elves:
                    ans += 1
        print(ans)
