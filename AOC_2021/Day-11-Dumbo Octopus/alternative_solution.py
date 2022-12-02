import numpy as np
from pprint import pprint


def part1():
    with open("AOC_2021\Day-11\input.txt", "r") as f:
        input = f.read().splitlines()
        print(input)

    ins = [[int(y) for y in list(x)] for x in input]

    flash_count = 0
    # NE - North East
    # NW - North West
    # SE - South East
    # SW - South West
    #       top    bottom  right  left    NE      NW      SE       SW
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for _ in range(100):
        for r in range(len(ins)):
            for c in range(len(ins[0])):
                ins[r][c] += 1

        changed = True
        while changed:
            changed = False
            for r in range(len(ins)):
                for c in range(len(ins[0])):
                    if ins[r][c] > 9:  # Greater than 9
                        flash_count += 1
                        # set to 0 once flashed
                        ins[r][c] = 0
                        changed = True
                        for dy, dx in dirs:
                            # Check your neighbours to make sure they are in the boundary
                            if r+dy < 0 or r+dy >= len(ins) or c+dx < 0 or c+dx >= len(ins[0]):
                                continue
                            if ins[r+dy][c+dx] == 0:
                                continue

                            ins[r + dy][c + dx] += 1
            pprint(ins)

    print(flash_count)


# part1()


def part2():
    with open("AOC_2021\Day-11\input.txt", "r") as f:
        input = f.read().splitlines()

    ins = [[int(y) for y in list(x)] for x in input]

    flash_count = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, 1), (1, -1), (-1, -1)]
    all_zero = False
    step = 0
    while not all_zero:
        for r in range(len(ins)):
            for c in range(len(ins[0])):
                ins[r][c] += 1

        changed = True
        while changed:
            changed = False
            for r in range(len(ins)):
                for c in range(len(ins[0])):
                    if ins[r][c] > 9:
                        flash_count += 1
                        ins[r][c] = 0
                        changed = True
                        for dy, dx in dirs:
                            if r+dy < 0 or r+dy >= len(ins) or c+dx < 0 or c+dx >= len(ins[0]):
                                continue
                            if ins[r+dy][c+dx] == 0:
                                continue
                            ins[r + dy][c + dx] += 1
        all_zero = True
        for r in range(len(ins)):
            for c in range(len(ins[0])):
                if ins[r][c] != 0:
                    all_zero = False
                    break
        if all_zero:
            print(step + 1)
            pprint(ins)
        step += 1


part2()
