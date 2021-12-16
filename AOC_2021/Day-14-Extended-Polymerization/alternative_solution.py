# %%
from collections import Counter

# %%
with open('sample.txt') as reader:
    line, _, *rest = reader.read().split('\n')
    # line = 'NNCB'
    first = line[0]
    # first = N
    start = Counter(map("".join, zip(line, line[1:])))
    # start = Counter({'NN': 1, 'NC': 1, 'CB': 1})
    data = dict(l.split(' -> ') for l in rest)
    # {'CH': 'B',
    #  'HH': 'N',
    #  'CB': 'H',
    #  'NH': 'C',
    #  'HB': 'C',
    #  'HC': 'B',
    #  'HN': 'C',
    #  'NN': 'C',
    #  'BH': 'H',
    #  'NC': 'B',
    #  'NB': 'B',
    #  'BN': 'B',
    #  'BB': 'N',
    #  'BC': 'B',
    #  'CC': 'N',
    #  'CN': 'C'}

# %%


def step(mp):
    print(data)
    n = Counter()
    for k, v in mp.items():
        print(f'n[k[0]+data[k]] = {n[k[0]+data[k]]}')
        n[k[0]+data[k]] = n[k[0]+data[k]] + v
        n[data[k]+k[1]] = n[data[k]+k[1]] + v
    return n


def solve(iters):
    data = start.copy()
    print(f'different data = {data}')
    for _ in range(iters):
        data = step(data)

    counts = Counter()
    for k, v in data.items():
        counts[k[1]] += v
    counts[first] += 1
    counts = counts.most_common()

    return counts[0][1] - counts[-1][1]


print("Part 1:", solve(10))
print("Part 2:", solve(40))


# %%
