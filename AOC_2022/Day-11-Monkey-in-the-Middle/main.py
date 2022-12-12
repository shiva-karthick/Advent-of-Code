import math

data = open('AOC_2022\Day-11-Monkey-in-the-Middle\\input.txt').read().strip()
lines = [x for x in data.split('\n')]


class Monkey():
    def __init__(self, id=None, items=None, operation=None, test_number=None, if_true_monkey=None, if_false_monkey=None, count=0):
        self.id = id
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.if_true_monkey = if_true_monkey
        self.if_false_monkey = if_false_monkey
        self.count = count

    def add_item(self, item: int):
        self.items.append(item)

    def print_data(self):
        print("Monkey id {}, items : {}, count : {} ".format(
            self.id, self.items, self.count))


# get the total number of monkeys
total_monkeys = len(data.split("\n\n"))

# create n number of monkey objects
monkey_list = [Monkey() for _ in range(total_monkeys)]

# collect all data here
for num, monkey in enumerate(data.split("\n\n")):
    # read for 1 monkey
    id_, items, op, test, true, false = monkey.strip().split('\n')
    monkey_list[num].id = id_[-2:-1]
    monkey_list[num].items = []  # decalre an empty list
    monkey_list[num].items.extend(
        [int(i) for i in items.split(':')[1].split(',')])
    monkey_list[num].operation = ''.join(op.split()[-2:])
    monkey_list[num].test_number = int(test.split()[-1])
    monkey_list[num].if_true_monkey = int(true.split()[-1])
    monkey_list[num].if_false_monkey = int(false.split()[-1])

for _ in range(0, 20):  # 20 rounds
    for m in range(0, total_monkeys):  # this constitutes 1 round
        # If a monkey is holding no items at the start of its turn, its turn ends.
        if len(monkey_list[m].items) == 0:
            continue
        for index in monkey_list[m].items:
            monkey_list[m].count += 1
            temp_str = str(index) + monkey_list[m].operation.replace(
                "old", str(index))
            new = eval(temp_str)
            # divide by 3, monkey is bored with item
            new = math.floor(new / 3)
            # check if divisible by test number
            if (new % monkey_list[m].test_number) == 0:  # is divisible; no remainder
                # throw to if_true_monkey
                # print("monkey_list[m].if_true_monkey = {}".format(
                #     monkey_list[m].if_true_monkey))
                monkey_list[monkey_list[m].if_true_monkey].add_item(
                    new)
            else:
                # print("monkey_list[m].if_false_monkey = {}".format(
                #     monkey_list[m].if_false_monkey))
                monkey_list[monkey_list[m].if_false_monkey].add_item(
                    new)
        monkey_list[m].items = []

for m in range(0, total_monkeys):
    print(monkey_list[m].print_data())

count = [0 for _ in range(total_monkeys)]
for i in range(total_monkeys):
    count[i] = monkey_list[i].count

print(sorted(count)[-1] * sorted(count)[-2])
