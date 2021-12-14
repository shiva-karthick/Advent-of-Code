# Day 3 Binary Diagnostic
# Part 1
# int(binary, 2), where binary is in string data type
import copy


def part1():
    lst = []
    with open(r"input.txt") as reader:
        for line in reader:
            lst.append(line.strip())

    # Store the number of 0s in a dictionary as a key-value pair.
    column_dict = {}

    # Initialise column_dict
    for i in range(len(lst[0])):
        column_dict[i] = 0

    for row in range(len(lst)):
        for column in range(len(lst[0])):
            if lst[row][column] == "0":
                column_dict[column] += 1

    print("column_dict = {}".format(column_dict))

    # Shows the number of 0s in every column
    gamma = "".join(list(map(lambda s: "0" if column_dict[s] > (
        len(lst) - column_dict[s]) else "1", column_dict)))
    print(gamma)

    gamma_int = int(gamma, 2)
    epsilon = gamma_int ^ 0xfff
    print(epsilon * gamma_int)


def part2():
    lst = []
    with open(r"input.txt") as reader:
        for line in reader:
            lst.append(line.strip())
    lst_2 = copy.deepcopy(lst)

    for i in range(len(lst[0])):
        if len(lst) == 1:
            break
        lst = list(filter(lambda s: s[i] if s[i] == "1" else [], lst)) if len(list(filter(lambda s: s[i] if s[i] == "1" else [], lst))) >= len(list(filter(lambda s: s[i] if
                                                                                                                                                           s[i] == "0" else [], lst))) else list(filter(lambda s: s[i] if s[i] == "0" else [], lst))
    oxygen_generator_rating = int(lst[0], 2)
    print(oxygen_generator_rating)

    for i in range(len(lst_2[0])):
        if len(lst_2) == 1:
            break
        lst_2 = list(filter(lambda s: s[i] if s[i] == "0" else [], lst_2)) if len(list(filter(lambda s: s[i] if s[i] == "0" else [], lst_2))) <= len(list(filter(lambda s: s[i] if
                                                                                                                                                                 s[i] == "1" else [], lst_2))) else list(filter(lambda s: s[i] if s[i] == "1" else [],  lst_2))
    co2_scrubber_rating = int(lst_2[0], 2)
    print(co2_scrubber_rating)

    print(co2_scrubber_rating * oxygen_generator_rating)
    # lst_3 = list(filter(lambda s: s[1] if s[1] == "1" else [], lst_2)) if len(list(filter(lambda s: s[1] if s[1] == "1" else [], lst_2))) >= len(list(filter(lambda s: s[1] if
    #                                                                                                                                                          s[1] == "0" else [], lst_2))) else list(filter(lambda s: s[1] if s[1] == "0" else [], lst_2))


part2()
