data = open('AOC_2022\Day-09-Rope-Bridge\input.txt').read().strip()
lines = [x for x in data.split('\n')]


def move(head, tail):
    delta_r = (head[0] - tail[0])
    delta_c = (head[1] - tail[1])

    # use absolute operator to get only the magnitude
    if abs(delta_r) <= 1 and abs(delta_c) <= 1:
        # if the change is less than or equals to 1; don't care it's already nearby
        pass
    elif abs(delta_r) >= 2 and abs(delta_c) >= 2:
        # move diagonal; this case occurs, have checked manually
        # there is only 2 possible scenarios
        if head[0] > tail[0]:
            tail = (head[0]-1, 0)
            if head[1] > tail[1]:
                tail = (tail[0], head[1] - 1)
            else:
                tail = (tail[0], head[1] + 1)
        elif head[0] < tail[0]:
            tail = (head[0]+1, 0)
            if head[1] > tail[1]:
                tail = (tail[0], head[1] - 1)
            else:
                tail = (tail[0], head[1] + 1)

    elif abs(delta_r) >= 2:
        if head[0] > tail[0]:
            tail = (head[0] - 1, head[1])
        else:
            tail = (head[0] + 1, head[1])

    elif abs(delta_c) >= 2:
        if head[1] > tail[1]:
            tail = (head[0], head[1] - 1)
        else:
            tail = (head[0], head[1] + 1)

    return tail


head = (0, 0)  # starting position
tail = [(0, 0) for _ in range(9)]

delta_r = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
delta_c = {'L': -1, 'U': 0, 'R': 1, 'D': 0}

P1 = set([tail[0]])
P2 = set([tail[8]])

for line in lines:
    direction, distance = line.split()
    distance = int(distance)
    for _ in range(distance):
        # move the head in the desired direction
        head = (head[0] + delta_r[direction], head[1] + delta_c[direction])

        # tail[0] is the most recently updated tuple
        tail[0] = move(head, tail[0])

        # part 2, update the rest of the snake
        for i in range(1, 9):  # 1, 2, 3, 4, 5, 6, 7, 8
            tail[i] = move(tail[i-1], tail[i])
        P1.add(tail[0])


print(len(P1))
print(len(P2))
