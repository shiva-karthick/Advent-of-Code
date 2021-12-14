# Path Finding with slightly modified version


# from collections import defaultdict
# from collections import deque

# graph = defaultdict(list)

# # Create a graph of source and destination as pairs
# with open('input.txt') as file:
#     for line in file.read().splitlines():
#         source, destination = line.split('-')
#         graph[source].append(destination)
#         graph[destination].append(source)
#     print(graph)

# smalls = set()


# def paths_to_end(node='start'):
#     if node == 'end':
#         return 1
#     if node in smalls:
#         return 0
#     if node.islower():
#         smalls.add(node)
#     count = sum(paths_to_end(neighbor) for neighbor in graph[node])
#     if node.islower():
#         smalls.remove(node)
#     return count


# print(paths_to_end())

# BFS solution
#maze = defaultdict(list)
# for s,e in re.findall(r'(.+)\-(.+)\n', open(filename).read()):
#    maze[s].append(e);maze[e].append(s)
#
# def bfs(start, goal):
#    node_queue = deque([(start,set(),True)])
#    while node_queue:
#        current,visited1,visited2 = node_queue.popleft()
#        if current == goal:
#            yield 1
#            continue
#        if current.islower():
#            visited2 &= current not in visited1
#            visited1.add(current)
#        for node in maze[current]:
#            if node not in visited1 or visited2 and node != start:
#                node_queue.append((node,visited1.copy(),visited2))
#print(sum(bfs('start', 'end')))
#
#
# maze = {
#    'start': ['A', 'b'],
#    'A': ['start', 'c', 'b', 'end'],
#    'b': ['start', 'A', 'd', 'end'],
#    'c': ['A'],
#    'd': ['b'],
#    'end': ['A', 'b']
# }
#


def dfs(start, goal, twice):
    queue = [(start, set(), twice)]
    while queue:
        # unpack the first and assign to the variables on the left
        current, small, twice = queue.pop()
        if current == goal:
            yield 1
        elif current.islower():
            twice &= current not in small
            small.add(current)
        for node in maze.get(current, []):
            if node not in small or twice:
                queue.append((node, small.copy(), twice))
#        print(queue)


maze = {}
for line in open("sample.txt").read().splitlines():
    s, e = line.split('-')
    if s != 'end' and e != 'start':
        maze.setdefault(s, set()).add(e)
    if e != 'end' and s != 'start':
        maze.setdefault(e, set()).add(s)

print(f"maze = {maze}")
print()

# print('part1', sum(dfs('start', 'end', 0)))
print('part2', sum(dfs('start', 'end', 1)))
