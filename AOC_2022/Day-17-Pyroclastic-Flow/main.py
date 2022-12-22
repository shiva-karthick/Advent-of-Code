# parse the input
data = open(r'AOC_2022\Day-17-Pyroclastic-Flow\input.txt').read().strip()
lines = [x for x in data.split('\n')]

# The tall, vertical chamber is exactly seven units wide.
# Each rock appears so that its left edge is two units away from the left wall
# and its bottom edge is three units above the highest rock in the room (or the floor, if there isn'rocks one).


def get_piece(rocks, y):  # set of (x,y) pairs
    '''
    5 different types of rocks
    ####

    .#.
    ###
    .#.

    ..#
    ..#
    ###

    #
    #
    #
    #

    ##
    ##
    '''
    if rocks == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif rocks == 1:
        return set([(3, y+2), (2, y+1), (3, y+1), (4, y+1), (3, y)])
    elif rocks == 2:
        return set([(2, y), (3, y), (4, y), (4, y+1), (4, y+2)])
    elif rocks == 3:
        return set([(2, y), (2, y+1), (2, y+2), (2, y+3)])
    elif rocks == 4:
        return set([(2, y+1), (2, y), (3, y+1), (3, y)])
    else:
        assert False


def move_left(piece):
    for (x, y) in piece:
        if x == 0:
            return piece
    else:
        return set([(x-1, y) for (x, y) in piece])


def move_right(piece):
    for (x, y) in piece:
        if x == 6:
            return piece
    else:
        return set([(x+1, y) for (x, y) in piece])


def move_down(piece) -> set:
    piece_ = set()  # create an empty set
    for (x, y) in piece:
        piece_.add((x, y - 1))
    return piece_


def move_up(piece):
    piece_ = set()  # create an empty set
    for (x, y) in piece:
        piece_.add((x, y + 1))
    return piece_


def show(floor):
    floor_y = max([y for (x, y) in floor])
    for y in range(floor_y, 0, -1):
        row = ''
        for x in range(7):
            if (x, y) in floor:
                row += '#'
            else:
                row += ' '
        print(row)

# part 2 code inspired from yt


def custom_func(floor):
    floor_y = max([y for (x, y) in floor])
    return frozenset([(x, floor_y-y) for (x, y) in floor if floor_y-y <= 1000])


floor = set([(x, 0) for x in range(7)])  # set of placed rocks

trillion_rocks = 1000000000000

SEEN = {}  # empty dictionary

result_1 = 0  # total units tall
index = 0
rocks = 0
added = 0

while rocks < trillion_rocks:
    #print(rocks, len(SEEN))
    # get 0 1 2 3 4 -> repeat 0 1 2 3 4
    piece = get_piece(rocks % 5, result_1 + 4)

    while True:

        # Move left or right
        if data[index] == '<':  # if left; push to the left
            piece = move_left(piece)
            if piece & floor:  # if the rock and floor has crashed, move the piece to the right
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & floor:  # if you move right into something, just move back left
                piece = move_left(piece)

        index = (index+1) % len(data)

        piece = move_down(piece)
        # if we collide with the floor (the floor moves up like an escalator)
        if piece & floor:
            piece = move_up(piece)  # move it back up
            floor |= piece  # add it to the floor formation
            result_1 = max([y for (x, y) in floor])  # recalculate the result_1

            # part 2
            SR = (index, rocks % 5, custom_func(floor))  # current situation
            if SR in SEEN and rocks >= 2022:
                # oldt is the last time when we are in the situation
                (oldt, oldy) = SEEN[SR]
                dy = result_1-oldy  # current result_1 - old result_1
                dt = rocks-oldt
                amt = (trillion_rocks-rocks)//dt
                added += amt*dy
                rocks += amt*dt
                assert rocks <= trillion_rocks
            SEEN[SR] = (rocks, result_1)
            # show(floor)
            break
    rocks += 1
    if rocks == 2022:
        print(result_1)  # height the y coordinate of the tallest rock

print(result_1+added)
