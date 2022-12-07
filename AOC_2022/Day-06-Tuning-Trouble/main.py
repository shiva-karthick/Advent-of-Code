data = open('AOC_2022\Day-06-Tuning-Trouble\input.txt').read()
test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

p1 = True

for i in range(len(data)):
    if (i - 3 >= 0) and len(set([data[i], data[i-1], data[i-2], data[i-3]])) == 4:
        print(i+1)
        p1 = False
        break

for i in range(len(data)):
    if (not p1) and (i - 13 >= 0) and len(set([data[i-j] for j in range(14)])) == 14:
        print(i+1)
        break
