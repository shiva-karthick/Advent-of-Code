import sys
import re
from collections import deque

next_elements, flow_rate = {}, {}

data = open(
    r'AOC_2022\Day-16-Proboscidea-Volcanium\\test_input.txt').read().strip()
lines = [x for x in data.split('\n')]

for line in lines:

    # get the line
    line = line.rstrip()

    # get the valve name
    u = line.split(' ')[1]

    # get the flow rate
    f = int(line.split(' ')[4].split('=')[1][:-1])

    # get the next elements
    vv = line.split('valve')[1].replace(
        's ', '').replace(' ', '').split(',')

    flow_rate[u] = f
    next_elements[u] = vv

# for line in lines:
#     res = re.findall(
#         'Valve (\w+) has flow rate=(\d+); tunnel[current_valve_at]* lead[current_valve_at]* to valve[current_valve_at]* ([\w\current_valve_at,]*)', line.strip())[0]
#     u, f, vv = res
#     f = int(f)
#     vv = vv.split(', ')
#     flow_rate[u] = f
#     next_elements[u] = vv

q = deque([(0, 'AA', [], 0)])
TIME = 30
states = set()
ps = {i: {} for i in range(TIME+1)}


while q:
    # the successor means (time+1, new_valve, new_opened_valves, total_pressure + pressure(opened_valves))
    # (time, current_valve_at, opened_valves, total_pressure)
    time, current_valve_at, opened_valves, total_pressure = q.popleft()
    # accurate: tuple(sorted(opened_valves))
    tup = (time, current_valve_at, total_pressure, len(opened_valves))
    if tup in states:
        continue
    states.add(tup)
    if time == TIME + 1:
        break
    ip = sum(map(flow_rate.get, opened_valves))
    tt = tuple(sorted(opened_valves))
    if time <= TIME:
        ps[time][tt] = max(ps[time].get(tt, 0), total_pressure)
    if current_valve_at not in opened_valves and flow_rate[current_valve_at] != 0:
        q.append((time+1, current_valve_at, opened_valves +
                 [current_valve_at], total_pressure+ip))
    for d in next_elements[current_valve_at]:
        q.append((time+1, d, opened_valves, total_pressure+ip))
ans = max(ps[30].values())
print('Part 1:', ans)

ans = max(ans, max(ps[26][i] + ps[26][j] for i in ps[26]
          for j in ps[26] if not set(i) & set(j)))
print('Part 2:', ans)
