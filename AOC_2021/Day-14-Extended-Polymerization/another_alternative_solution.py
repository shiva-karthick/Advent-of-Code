from collections import Counter
import parse


filename = "sample.txt"

# Less optimised

# with open(filename) as f:
#     aoc_input = f.read()
# s, rules = aoc_input.split('\n\n')
# rules = dict(parse.findall('{:w} -> {:l}', rules))
# counts = dict((k, s.count(k)) for k in rules)
# elements = Counter(s)
# for step in range(1, 41):
#     tcounts, counts = counts, Counter()
#     for (a, b), k in rules.items():
#         counts[a+k] += tcounts[a+b]
#         counts[k+b] += tcounts[a+b]
#         elements[k] += tcounts[a+b]
#     if step in (10, 40):
#         print(elements.most_common()[0][1]-elements.most_common()[-1][1])

# More optimised : edit found a way to get rid of the counter swapping

with open(filename) as f:
    s, aoc_input = f.read().split('\n\n')

# Dictionary translation
rules = dict(parse.findall('{:w} -> {:l}', aoc_input))
counts = dict((k, s.count(k))
              for k in rules)  # Stores the counts of the 'NNCB'
elements = Counter(s)

for step in range(1, 41):
    tmp = [(a, b, k, counts[a+b]) for (a, b), k in rules.items()]
    print(tmp)
    for a, b, k, c in [(a, b, k, counts[a+b]) for (a, b), k in rules.items()]:
        counts[a+b] -= c
        counts[a+k] += c
        counts[k+b] += c
        elements[k] += c
    if step in (10, 40):
        print(elements.most_common()[0][1]-elements.most_common()[-1][1])
