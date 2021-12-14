
# Overview of the solution, can use either dfs or bfs

step 1): read the data into some sort of graph (I used a dictionary of lists where the lists were where you could go to)

step 2): start at start as the current node, if it's the goal, you have a path, if not, explore every child node of the current node. keep track of what nodes cannot be revisited.

step 3) display how many paths you found

## BFS solution
1. parse the data into a dict as a key , with all its neighbour in an iterable as value
2. bfs(start,end)

``` python

from collections import defaultdict

maze = collections.defaultdict(list)
for s,e in re.findall(r'(.+)\-(.+)\n', open(filename).read()):
    maze[s].append(e);maze[e].append(s)
print(sum(bfs('start', 'end')))
```
