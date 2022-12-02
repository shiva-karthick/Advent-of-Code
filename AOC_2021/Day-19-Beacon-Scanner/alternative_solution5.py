"""
Advent of Code 2021 - Day 19
https://adventofcode.com/2021/day/19
"""

import re
from math import sqrt
from typing import Dict, List, Tuple, Any


FULL_INPUT_FILE = f'AOC_2021\Day-19\sample.txt'


def load_data(infile_path: str) -> Dict[int, Dict[int, Dict[int, Dict[str, int]]]]:
    with open(infile_path, 'r', encoding='ascii') as infile:
        data = {}
        current_scanner = None
        for line in infile:
            if line.startswith('--- scanner '):
                current_scanner = int(re.search(r'\d+', line).group())
                data[current_scanner] = {}
                count = 0
            elif line.strip():
                data[current_scanner][count] = {
                    'loc': [int(i) for i in line.split(',')]}
                count += 1
    return data


def build_map(infile_path: str) -> Tuple[Dict[int, Dict[int, Dict[str, int]]], List[List[int]]]:
    scanners = load_data(infile_path)
    for s in scanners:
        calculate_distances(scanners[s])
    offsets = []
    while len(scanners) > 1:
        matches = find_matches(scanners)
        offsets.append(transform_and_merge(matches, scanners))
        del scanners[matches[0]['s2']]
        calculate_distances(scanners[matches[0]['s1']])
    return scanners[0], offsets


def transform_and_merge(matches: List[Dict[str, int]], scanners: Dict[int, Any]) -> List[int]:
    dest = matches[0]['s1']
    src = matches[0]['s2']

    dest_a, dest_b, dest_diff, src_a, src_b, src_diff = [None] * 6

    n = 0
    usable = False
    while not usable:
        n += 1
        dest_a, dest_b = [scanners[dest][matches[i]['b1']]['loc']
                          for i in (0, n)]
        src_a, src_b = [scanners[src][matches[i]['b2']]['loc'] for i in (0, n)]
        dest_diff = [dest_a[i] - dest_b[i] for i in (0, 1, 2)]
        src_diff = [src_a[i] - src_b[i] for i in (0, 1, 2)]
        if len(set(dest_diff)) == 3 and len(set(src_diff)) == 3 and 0 not in src_diff and 0 not in dest_diff:
            usable = True

    src_idx = [src_diff.index(dest_diff[i]) if dest_diff[i] in src_diff
               else src_diff.index(dest_diff[i] * -1) for i in (0, 1, 2)]
    src_orientation = [dest_diff[i] / src_diff[src_idx[i]] for i in (0, 1, 2)]
    offset = [dest_a[i] - (src_a[src_idx[i]] * src_orientation[i])
              for i in (0, 1, 2)]
    known_beacons = [scanners[0][i]['loc'] for i in scanners[0]]
    for b in scanners[src]:
        xformed_beacon = [int(scanners[src][b]['loc'][src_idx[i]] * src_orientation[i] + offset[i])
                          for i in (0, 1, 2)]
        if xformed_beacon not in known_beacons:
            scanners[dest][len(scanners[dest])] = {'loc': xformed_beacon}
    return offset


def find_matches(scanners: Dict[int, Any]) -> List[Dict[str, int]]:
    matches = []
    for s1 in scanners:
        for s2 in [sx for sx in scanners if sx > s1]:
            for b1 in scanners[s1]:
                b1_ds = scanners[s1][b1]['distance_set']
                for b2 in scanners[s2]:
                    b2_ds = scanners[s2][b2]['distance_set']
                    if len(b1_ds.intersection(b2_ds)) >= 11:
                        matches.append(
                            {'s1': s1, 'b1': b1, 's2': s2, 'b2': b2})
                        if len(matches) == 12:
                            return matches
    return matches


def calculate_distances(scanner: Dict[int, Any]) -> None:
    for b1 in scanner:
        x1, y1, z1 = scanner[b1]['loc']
        scanner[b1]['distance_set'] = set()
        for b2 in [bx for bx in scanner if bx != b1]:
            x2, y2, z2 = scanner[b2]['loc']
            distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
            scanner[b1]['distance_set'].add(distance)


def find_longest_distance(offsets:  List[List[int]]) -> int:
    m = 0
    for i in range(len(offsets)):
        for j in range(i + 1, len(offsets)):
            n = sum([abs(offsets[i][k] - offsets[j][k]) for k in (0, 1, 2)])
            m = n if n > m else m
    return int(m)


def part_1_and_2(infile_path: str):
    beacons, offsets = build_map(infile_path)
    part1_answer = len(beacons)
    part2_answer = find_longest_distance(offsets)

    print(f'Part 1: {part1_answer}')
    print(f'Part 2: {part2_answer}')


if __name__ == '__main__':
    part_1_and_2(FULL_INPUT_FILE)
