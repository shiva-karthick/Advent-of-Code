data = open('AOC_2022\Day-05-Supply-Stacks\input.txt').read()
lines = [x for x in data.split('\n')]

queues = []
commands = []

# 1. create a list of all the lists; Fantastic solution
for line in lines:
    if line == '':  # separate the commands and the actual queues
        break
    total_queues = (len(line)+1) // 4  # get the number of queues
    while len(queues) < total_queues:  # append 9 lists in 1 big list
        queues.append([])
    for i in range(len(queues)):  # i is from 0 to 8
        ch = line[1 + 4 * i]  # 1, 5, 9, 13, 17, 21, 25, 29, 33
        if ch != ' ' and 'A' <= ch <= 'Z':  # sanity check to make sure its not an empty char and between A and Z
            queues[i].append(ch)

for cmd in lines[10:]:
    if cmd == "":
        break
    phrase = cmd.split(' ')
    number_of_letters = int(phrase[1])
    source = int(phrase[3]) - 1
    destination = int(phrase[5]) - 1

    # Extract the required characters
    transfer_list = queues[source][:number_of_letters]
    # Update the old queue
    queues[source] = queues[source][number_of_letters:]
    # Reverse the transfer_list and join the transfer list at the beginning of the destination queue
    # queues[destination] = list(
    #     reversed(transfer_list)) + queues[destination][:]
    # part 2
    # Join the transfer list at the beginning of the destination queue
    queues[destination] = transfer_list + queues[destination][:]

print(''.join([s[0] for s in queues if len(queues) > 0]))
