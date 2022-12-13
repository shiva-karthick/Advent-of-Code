from functools import cmp_to_key


def compare(a, b) -> int:
    if isinstance(a, int) and isinstance(b, list):
        a = [a]
    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        return -1 if a < b else 1
    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if (result := compare(x, y)) != 0:
                return result
        if len(a) == len(b):
            return 0
        return -1 if len(a) < len(b) else 1
    raise TypeError


def part1(packets):
    return sum(
        i + 1 for i, (a, b) in enumerate(packets)
        if compare(a, b) == -1
    )


def part2(data):
    packets = [[[2]], [[6]]]
    for pack in data:
        packets.extend(pack)

    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


if __name__ == '__main__':
    s = open("AOC_2022\Day-13-Distress-Signal\input.txt").read().strip().split('\n\n')
    parsed = [[*map(eval, ln.splitlines())] for ln in s]
    print(parsed)
    print('Part 1:', part1(parsed))
    print('Part 2:', part2(parsed))
