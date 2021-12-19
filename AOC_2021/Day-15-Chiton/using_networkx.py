import networkx as nx

filename = "AOC_2021\Day-15-Chiton\sample.txt"
with open(filename) as f:
    aoc_input = [list(map(int, line)) for line in f.read().splitlines()]


def make_big(aoc_input):
    h, w = len(aoc_input), len(aoc_input[0])
    for i in range(h):
        for p in range(w, 5*w):
            aoc_input[i].append(aoc_input[i][p-w] % 9+1)
    for i in range(h, 5*h):
        aoc_input.append([aoc_input[i-h][p] % 9+1 for p in range(5*w)])


def get_risk(aoc_input):
    chitons = {(i, j): c for i, row in enumerate(aoc_input)
               for j, c in enumerate(row)}

    def neighbors(x, y): return [
        (x+dx, y+dy)for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]if(x+dx, y+dy) in chitons]
    cave = nx.DiGraph()
    cave.add_edges_from(
        ((x, y), n, {'weight': chitons[n]}) for x, y in chitons for n in neighbors(x, y))
    return nx.dijkstra_path_length(cave, (0, 0), (len(aoc_input)-1, len(aoc_input[0])-1), weight='weight')


print('part1', get_risk(aoc_input))
make_big(aoc_input)
print('part2', get_risk(aoc_input))
