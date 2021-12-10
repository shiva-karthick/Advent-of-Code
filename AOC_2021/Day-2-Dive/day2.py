def part1():
    # Initialise the variables
    depth = 0
    width = 0

    # Read file line by line
    with open(r"input.txt") as reader:
        for line in reader:
            command = line.strip().split()[0][0]
            if command == "f":
                width += int(line.strip().split()[1])
            elif command == "d":
                depth += int(line.strip().split()[1])
            elif command == "u":
                depth -= int(line.strip().split()[1])
    print(f"width = {width}, depth = {depth}")
    print(width*depth)


def part2():
    # Initialise variables
    depth = 0
    width = 0
    aim = 0

    with open(r"input.txt") as reader:
        for line in reader:
            command = line.strip().split()[0][0]
            if command == "d":
                aim += int(line.strip().split()[1])
            elif command == "u":
                aim -= int(line.strip().split()[1])
            else:
                # increase horizontal position by X units
                width += int(line.strip().split()[1])
                depth += aim * int(line.strip().split()[1])
        print(
            f'horizontal position = {width}, depth = {depth}, {width * depth}')


part1()
part2()
