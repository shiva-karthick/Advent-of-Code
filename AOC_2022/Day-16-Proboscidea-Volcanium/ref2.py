import re
from collections import deque


def bfs(tunnels, start, targets):  # bfs(tunnels, start, flow_rate)
    dist = {start: 0}
    seen = {start}
    q = deque([start])
    # In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, any() returns False. If at least one key is true, any() returns True.
    while q and any(t not in dist for t in targets):
        p = q.popleft()
        for x in tunnels[p]:  # tunnels['AA'] = ['DD', 'II', 'BB']
            if x not in seen:
                seen.add(x)
                dist[x] = dist[p] + 1
                q.append(x)
    return dist


def find_paths(dist, flow_rate, t):
    pressures = []
    paths = []
    stack = [(t, 0, ['AA'])]
    while stack:
        t, p, path = stack.pop()
        cur = path[-1]
        new = []
        for n, d in dist[cur].items():
            if d > t - 2 or n in path:
                continue
            tt = t - d - 1
            pp = p + flow_rate[n] * tt
            s = tt, pp, path + [n]
            new.append(s)
        if new:
            stack.extend(new)
        else:
            pressures.append(p)
            # paths always start at AA, so no need to keep first location
            paths.append(path[1:])
    return pressures, paths


def solve():

    # parsing the input
    flow_rate = {}
    tunnels = {}
    for line in open('AOC_2022\Day-16-Proboscidea-Volcanium\\test_input.txt').read().splitlines():
        _, valve, *_ = line.split()
        r = int(line.split()[4].split('=')[1].split(";")[0])
        if r:  # use only non zero values
            flow_rate[valve] = r
        m = re.search(r'valves? (.+)$', line).group(1)
        tunnels[valve] = m.split(', ')

    # Part One
    dist = {}
    for start in ('AA', *flow_rate):  # *flow_rate = BB CC DD EE HH JJ
        dist[start] = {}
        d = bfs(tunnels, start, flow_rate)
        for r in flow_rate:
            if r != start and r in d:
                dist[start][r] = d[r]

    p, _ = find_paths(dist, flow_rate, 30)
    print(max(p))

    # Part Two
    # x = list(zip(*find_paths(dist, flow_rate, 26)))
    # p, paths = zip(*sorted(x, reverse=True))
    # i, j = 0, 1
    # while any(x in paths[j] for x in paths[i]):
    #     j += 1
    # ans = p[i] + p[j]  # lower bound
    # j_max = j  # since p[i] can only decrease, j cannot exceed this
    # for i in range(1, j_max):
    #     for j in range(i + 1, j_max + 1):
    #         if any(x in paths[j] for x in paths[i]):
    #             continue
    #         ans = max(ans, p[i] + p[j])
    # print(ans)


solve()
