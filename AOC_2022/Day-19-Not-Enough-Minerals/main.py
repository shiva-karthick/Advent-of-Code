from collections import defaultdict, deque
import os
import sys

data = open('AOC_2022\Day-19-Not-Enough-Minerals\input.txt').read().strip()
lines = [x for x in data.split('\n')]


def solve(ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_cost_ore, geode_cost_clay, time):

    best = 0

    # Keep track of the states!
    # state is (ore, clay, obsidian, geodes, robot_1, robot_2, robot_3, robot_4, time)
    S = (0, 0, 0, 0, 1, 0, 0, 0, time)

    queue = deque([S])

    seen = set()

    while queue:
        state = queue.popleft()
        # print(state)
        ore, clay, obsidian, geodes, robot_1, robot_2, robot_3, robot_4, time = state

        best = max(best, geodes)  # get the maximum number

        if time == 0:
            continue

        # Optimisation;
        # I "just" did a BFS, but you need some optimizations to make it faster.
        # My main idea is to "throw away" extra resources ( and robots) -
        # for example if you can only spend at most 4 ore per minute, there's no point having 5 ore robots.
        # Similarly, if you have so much ore you could never spend it all, you can just throw away the excess.
        # This compresses the state space enough to make the BFS run quickly.

        optimised = max([ore_robot_cost, clay_robot_cost,
                         obsidian_robot_ore_cost, geode_cost_ore])  # get the maximum value

        if robot_1 >= optimised:
            robot_1 = optimised

        if robot_2 >= obsidian_robot_clay_cost:
            robot_2 = obsidian_robot_clay_cost

        if robot_3 >= geode_cost_clay:
            robot_3 = geode_cost_clay

        if ore >= time * optimised - robot_1 * (time - 1):
            ore = time * optimised - robot_1 * (time - 1)
        if clay >= time * obsidian_robot_clay_cost - robot_2 * (time - 1):
            clay = time * obsidian_robot_clay_cost - robot_2 * (time - 1)
        if obsidian >= time * geode_cost_clay - robot_3 * (time - 1):
            obsidian = time * geode_cost_clay - robot_3 * (time - 1)

        state = (ore, clay, obsidian, geodes, robot_1,
                 robot_2, robot_3, robot_4, time)

        if state in seen:
            continue

        seen.add(state)

        # collect resources for all of your robots; don't buy robot
        queue.append((ore + robot_1, clay + robot_2, obsidian + robot_3,
                      geodes + robot_4, robot_1, robot_2, robot_3, robot_4, time - 1))

        # buy robots and pay for them
        if ore >= ore_robot_cost:  # buy ore robot and pay for it
            queue.append((ore - ore_robot_cost + robot_1, clay + robot_2, obsidian +
                          robot_3, geodes + robot_4, robot_1 + 1, robot_2, robot_3, robot_4, time - 1))

        if ore >= clay_robot_cost:  # buy clay robot and pay for it
            queue.append((ore - clay_robot_cost + robot_1, clay + robot_2, obsidian +
                          robot_3, geodes + robot_4, robot_1, robot_2 + 1, robot_3, robot_4, time - 1))

        if ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost:
            queue.append((ore - obsidian_robot_ore_cost + robot_1, clay -
                          obsidian_robot_clay_cost + robot_2, obsidian + robot_3, geodes + robot_4, robot_1, robot_2, robot_3 + 1, robot_4, time-1))

        if ore >= geode_cost_ore and obsidian >= geode_cost_clay:
            queue.append((ore - geode_cost_ore + robot_1, clay + robot_2, obsidian -
                          geode_cost_clay + robot_3, geodes + robot_4, robot_1, robot_2, robot_3, robot_4 + 1, time - 1))
    return best


result_1 = 0
result_2 = 1
for i, line in enumerate(lines):
    words = line.split()
    id_ = int(words[1][:-1])
    ore_robot_cost = int(words[6])
    clay_robot_cost = int(words[12])
    obsidian_robot_ore_cost, obsidian_robot_clay_cost = int(
        words[18]), int(words[21])
    geode_cost_ore, geode_cost_clay = int(words[27]), int(words[30])

    s1 = solve(ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost,
               obsidian_robot_clay_cost, geode_cost_ore, geode_cost_clay, 24)
    result_1 += id_*s1

    if i < 3:
        s2 = solve(ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost,
                   obsidian_robot_clay_cost, geode_cost_ore, geode_cost_clay, 32)
        result_2 *= s2
print(result_1)
print(result_2)
