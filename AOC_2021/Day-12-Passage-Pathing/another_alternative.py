# - can only visit 1 lower case twice
# - can revisit upper case
# - cannot revisit start
# - what are all the points from the start to end

# https: // www.youtube.com/watch?v = dlPoe04FoQk

import collections

edges = collections.defaultdict(set)
with open("sample.txt") as reader:
    for line in reader:
        line = line.strip()
        src, dst = line.split('-')
        edges[src].add(dst)
        edges[dst].add(src)
print(edges)

done = set()

todo = [(('start',), False)]
while todo:
    path, double_small = todo.pop()
    if path[-1] == 'end':
        done.add(path)
        continue

    for choice in edges[path[-1]] - {'start'}:
        if choice.isupper():
            todo.append(((*path, choice), double_small))
        elif double_small is False and path.count(choice) == 1:
            todo.append(((*path, choice), True))
        elif choice not in path:
            todo.append(((*path, choice), double_small))

print(len(done))
