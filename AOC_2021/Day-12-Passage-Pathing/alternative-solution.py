from typing import Dict
# from helper import get_input
from collections import Counter, defaultdict

inp = defaultdict(list)
with open("sample.txt") as reader:
    for x in reader:
        x = x.strip()
        inp[x.split('-')[0]].append(x.split('-')[1])
        inp[x.split('-')[1]].append(x.split('-')[0])
print(inp)


def get_paths(i: Dict[str, str], prev_path: list = ["start"]):
    paths = []
    for node in i[prev_path[-1]]:
        if node == "start":
            continue
        if node == "end":
            paths.append(prev_path + ["end"])
            continue
        if node.islower():
            new_i = defaultdict(list)
            for key in i.keys():
                for v in i[key]:
                    if v == node:
                        continue
                    new_i[key].append(v)
            for x in get_paths(new_i, prev_path + [node]):
                paths.append(x)
        else:
            for x in get_paths(i, prev_path + [node]):
                paths.append(x)

    return paths


def part_one():
    return len(get_paths(inp))


def get_paths_rpt(i: Dict[str, str], prev_path: list = ["start"]):
    paths = []
    for node in i[prev_path[-1]]:
        if node == "start":
            continue
        if node == "end":
            paths.append(prev_path + ["end"])
            continue
        if node.islower():
            cntr = Counter(prev_path)
            if node not in prev_path:
                for x in get_paths_rpt(i, prev_path + [node]):
                    paths.append(x)
                continue
            if cntr[node] == 1:
                if any([cntr[x] == 2 for x in cntr.keys() if x.islower() and x != node]):
                    continue
                new_i = defaultdict(list)
                for key in i.keys():
                    for v in i[key]:
                        if v == node:
                            continue
                        new_i[key].append(v)
                for x in get_paths_rpt(new_i, prev_path + [node]):
                    paths.append(x)
        else:
            for x in get_paths_rpt(i, prev_path + [node]):
                paths.append(x)

    return paths


def part_two():
    return len(get_paths_rpt(inp))


# print(f"Part one = {part_one()}")
print(f"Part two = {part_two()}")
