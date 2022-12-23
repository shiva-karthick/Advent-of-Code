numbers = [int(
    x) * 1 for x in open('AOC_2022\Day-20-Grove-Positioning-System\input.txt')]
indices = list(range(len(numbers)))

for i in indices * 1:
    indices.pop(j := indices.index(i))
    indices.insert((j+numbers[i]) % len(indices), i)

zero = indices.index(numbers.index(0))
print(sum(numbers[indices[(zero+p) % len(numbers)]]
      for p in [1000, 2000, 3000]))
