filename = 'AOC_2021\Day-20-Trench-Map\input.txt'

code, imagem = open(filename).read().split('\n\n')


code, imagem = ['.#'.index(c) for c in code], imagem.splitlines()

points = [(x, y) for y in range(-55, len(imagem)+55)
          for x in range(-55, len(imagem[0])+55)]

imagem = {(x, y): '.#'.index(c) for y, row in enumerate(imagem)
          for x, c in enumerate(row)}


def getbin(x, y, d):
    return int(''.join(''.join('01'[imagem.get((n, y), d)] for n in range(x-1, x+2)) for y in range(y-1, y+2)), 2)


for i in range(2):
    imagem = {(x, y): code[getbin(x, y, i % 2)] for x, y in points}

print('part1:', sum(imagem[loc] for loc in imagem))

for i in range(48):
    imagem = {(x, y): code[getbin(x, y, i % 2)] for x, y in points}

print('part2:', sum(imagem[loc] for loc in imagem))
