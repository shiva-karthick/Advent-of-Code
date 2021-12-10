import numpy as np

# these are for list of ints with -> in the middle:
aoc_input = np.loadtxt(re.sub(r'(\d+),(\d+) -> (\d+),(\d+)',
                       r'\1 \2 \3 \4', open(filename).read()).splitlines(), int)\

aoc_input = ((map(int, line)) for line in re.findall(
    r'(\d+),(\d+) -> (\d+),(\d+)', open(filename).read()))

aoc_input = [list(map(int, i.replace(",", " ").replace(
    " -> ", " ").split())) for i in open(filename)]

aoc_input = np.loadtxt(re.findall(
    r'(\d+)', open(filename).read()), int).reshape((-1, 4))

aoc_input = [eval(x.replace('->', ','))for x in open(filename)]

aoc_input = np.fromregex(open(filename), '\d+', [('', int)]*4)

# these are just for list of ints:
aoc_input = np.fromfile(open(filename), int, sep=',')
aoc_input = [eval(x)for x in open(filename)]
aoc_input = eval(open(filename).read())
