from collections import Counter

with open('sample.txt') as reader:
    line, _, *rest = reader.read().split('\n')
    # line = 'NNCB'
    first = line[0]
    # first = N
    start = list(map("".join, zip(line, line[1:])))
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

output = ""
# slice in pairs
for _ in range(10):
    for index in range(len(start)):
        start[index] = start[index][0] + data[start[index]] + start[index][1]
    for index in range(1, len(start)):
        start[index] = start[index][1:]
    start = "".join(start)
    output = start
    start = list(map("".join, zip(start, start[1:])))

print(Counter(output))
