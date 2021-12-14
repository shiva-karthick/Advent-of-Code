#!/usr/bin/python3


def part1():
    d = dict()
    with open(r"input.txt") as reader:
        lst = map(int, reader.read().split(","))

    # Init the dictionary d
    for i in range(9):
        d[i] = 0

    for i in list(lst):
        d[i] += 1

    for _ in range(80):
        new_fishes = d[0]

        # Queue FIFO
        for i in range(8):
            d[i] = d[i+1]

        d[8] = new_fishes
        d[6] += new_fishes

    print(sum(map(lambda x : d[x], d)))
part1()
