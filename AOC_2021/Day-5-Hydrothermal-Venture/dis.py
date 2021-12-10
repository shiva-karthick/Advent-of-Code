from collections import defaultdict


def sort_low_high(start, end):
    start, end = min(start, end), max(start, end)
    return start, end


with open(r"input.txt") as file_hnd:
    grid = defaultdict(int)
    lines = file_hnd.read().split("\n")
    for line in lines:
        start, end = line.split(" -> ")
        start, end = start.split(","), end.split(",")
        start_x, start_y = map(int, start)
        end_x, end_y = map(int, end)
        if start_x == end_x:
            start_y, end_y = sort_low_high(start_y, end_y)
            distance_range = end_y - start_y + 1
            for i in range(distance_range):
                current_y = start_y + i
                grid[f"{start_x},{current_y}"] += 1
        elif start_y == end_y:
            start_x, end_x = sort_low_high(start_x, end_x)
            distance_range = end_x - start_x + 1
            for i in range(distance_range):
                current_x = start_x+i
                grid[f"{current_x},{start_y}"] += 1
        else:
            distance_range = max(start_y, end_y) - min(start_y, end_y) + 1
            for i in range(distance_range):
                if start_x < end_x:
                    current_x = start_x + i
                else:
                    current_x = start_x - i
                if start_y < end_y:
                    current_y = start_y + i
                else:
                    current_y = start_y - i
                grid[f"{current_x},{current_y}"] += 1
overlaps = sum(v > 1 for v in grid.values())
print(overlaps)
