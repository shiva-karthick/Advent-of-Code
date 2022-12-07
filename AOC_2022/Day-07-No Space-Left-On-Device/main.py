import sys
from collections import defaultdict
# infile = sys.argv[1] if len(sys.argv) > 1 else '7.in'
data = open('AOC_2022\Day-07-No Space-Left-On-Device\input.txt').read().strip()

test_data = """ $ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

lines = [x for x in data.split('\n')]


# Avoid the key error, provide a default value for the key that does not exist
directory_size = defaultdict(int)
LIFO_data_struct = []  # Last In First Out data structure


for line in lines:
    # Check for cd command and move into that directory
    cmd = line.strip().split()
    if cmd[1] == "cd":
        if cmd[2] == '..':
            LIFO_data_struct.pop()
        else:
            LIFO_data_struct.append(cmd[2])  # append '/' or 'directory'
    elif cmd[1] == "ls":
        continue  # just ignore ls command
    elif cmd[0] == "dir":
        continue  # just ignore dir command
    else:
        size = int(cmd[0])
        # Most important information
        # Add this file's size to the current directory size *and* the size of all parents
        for i in range(1, len(LIFO_data_struct) + 1):
            directory_size['|===>|'.join(LIFO_data_struct[:i])] += size
p1 = 0
p2 = 1e9
max_space_to_be_used = 70000000 - 30000000
total_used = directory_size['/']
need_to_free = total_used - max_space_to_be_used

for key, value in directory_size.items():
    if (value <= 100000):
        p1 += value
    if value >= need_to_free:
        if p2 > value:
            p2 = value
    print(key, value)

print(f"Part 1 answer : {p1} \n")
print(f"Part 2 answer : {p2} \n")
