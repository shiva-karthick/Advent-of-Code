from copy import deepcopy
from math import prod
# from more_itertools import chunked, ilen
from collections import Counter, defaultdict
from heapq import heappush, heappop
# from tqdm import tqdm
from time import perf_counter
from contextlib import contextmanager
from functools import cache, lru_cache
import re
import statistics as stat
import sys
from queue import PriorityQueue


def infile(filename):
    if len(sys.argv) < 2:
        return 'input/'+filename
    return sys.argv[1]


def parse_block_grid(text, apply_fn=int):
    grid = [[apply_fn(x) for x in row.strip()] for row in text.splitlines()]
    return grid, len(grid[0]), len(grid)


def get_lines(file):
    return [line.strip() for line in file.readlines()]


def get_all_ints(text):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def grid_to_dict(grid):
    return {(i, j): v for j, row in enumerate(grid) for i, v in enumerate(row)}


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


def drange(start, stop):
    if start > stop:
        return range(stop, start-1, -1)
    else:
        return range(start, stop+1)


def span_list(lst):
    return (min(lst), max(lst))


def range_span(lst):
    mn, mx = span_list(lst)
    return range(mn, mx+1)


@contextmanager
def timer(s) -> float:
    start = perf_counter()
    yield
    end = perf_counter()
    print(f"{s}: {end - start:.5f}s")


def shiftmod(n, m, shift=1):
    """
    Simlar to n % m except the result lies within [shift, m + shift).

    Example:
        shiftmod(10, 10, shift=1) == 10
        shiftmod(11, 10, shift=1) == 1
        shiftmod(11, 10, shift=2) == 11
        shiftmod(12, 10, shift=2) == 2
    """
    return (n - shift) % m + shift
