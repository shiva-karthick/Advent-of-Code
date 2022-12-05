with open("input.txt") as f:
    inpt = f.read().split("\n\n")

a = sorted(map(lambda x: sum(map(int, x.split("\n"))), inpt))
print(a[-1])
print(a[-1] + a[-2] + a[-3])