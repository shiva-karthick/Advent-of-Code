
test_data = """30373
25512
65332
33549
35390"""

data = open('AOC_2022\Day-08-Treetop-Tree-House\input.txt').read().strip()

lines = [x for x in data.split('\n')]

lis = []
for line in lines:
    row = line
    lis.append(row)

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rows = len(lis)
columns = len(lis[0])


def part1() -> int:
    result = 0

    for r in range(0, rows):  # Loop all the rows
        for c in range(0, columns):  # Loop all the columns
            is_visible = False  # check if visible
            for (dr, dc) in directions:
                new_r = r  # update the new r
                new_c = c  # update the new c
                check_flags = True

                while True:
                    new_r += dr
                    new_c += dc
                    # if the coordinate is out of the boundaries, break
                    if not (0 <= new_r < rows and 0 <= new_c < columns):
                        break
                    if lis[new_r][new_c] >= lis[r][c]:
                        check_flags = False

                if check_flags:  # once the tree can be seen, set the has_reached_the_end to be visible
                    is_visible = True
            if is_visible:
                result += 1

    return result


def part2():
    counter = 0
    old_temp = 1
    result = []

    for r in range(0, rows):  # Loop all the rows
        for c in range(0, columns):  # Loop all the columns
            old_temp = 1
            for (dr, dc) in directions:
                new_r = r  # update the new r
                new_c = c  # update the new c
                has_reached_the_end = 0
                counter = 0  # reset the variable

                while True:
                    new_r += dr
                    new_c += dc

                    # if the coordinate is out of the boundaries, break
                    if not (0 <= new_r < rows and 0 <= new_c < columns):
                        break
                    # print(lis[new_r][new_c])
                    if has_reached_the_end:
                        break
                    if lis[new_r][new_c] < lis[r][c]:
                        counter += 1
                    elif lis[new_r][new_c] >= lis[r][c]:
                        has_reached_the_end = 1
                        counter += 1

                if counter != 0:
                    old_temp = counter * old_temp
            result.append(old_temp)
    return result


print(max(part2()))
