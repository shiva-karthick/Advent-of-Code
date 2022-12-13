from collections import defaultdict, deque
from copy import deepcopy
from functools import cmp_to_key
from pprint import pprint

data = open("AOC_2022\Day-13-Distress-Signal\input.txt").read().strip()
lines = [x for x in data.split('\n')]


def cmp(left, right) -> bool:

    if isinstance(left, int) and isinstance(right, list):
        # convert the integer to a list which contains that integer as its only value, then retry the comparison.
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        # convert the integer to a list which contains that integer as its only value, then retry the comparison.
        right = [right]

    # Base Case
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            # Otherwise, the inputs are the same integer; continue checking the next part of the input.
            return 0
        else:
            return -1 if left < right else 1

    if isinstance(left, list) and isinstance(right, list):
        for x, y in zip(left, right):
            c = cmp(x, y)
            if c == -1:
                return -1
            if c == 1:
                return 1
        # If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
        if len(left) == len(right):
            return 0
        # If the right list runs out of items first, the inputs are not in the right order.
        return -1 if len(left) < len(right) else 1
    raise TypeError


packets = []
result_1 = 0
for index, group in enumerate(data.split('\n\n')):
    left, right = group.split("\n")
    # eval is a good choise here
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
    if cmp(left, right) == -1:
        result_1 += 1 + index

print(f"{result_1}")
