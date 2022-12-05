X = [l.strip() for l in open('AOC_2022\Day-02-Rock-Paper-Scissors\input.txt')]

p1 = 0
p2 = 0

for x in X:
    op, me = x.split()  # split 'B Z'

    # points system for the chosen rock or paper or scissor
    p1 += {'X': 1, 'Y': 2, 'Z': 3}[me]
    # place a dictionary to choose from every permutation
    p1 += {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
           ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
           ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
           }[(op, me)]

    p2 += {'X': 0, 'Y': 3, 'Z': 6}[me]
    p2 += {('A', 'X'): 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
           ('B', 'X'): 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
           ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
           }[(op, me)]
print(p1)
print(p2)
