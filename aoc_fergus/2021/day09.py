from aocd import lines
from functools import reduce
from operator import mul

grid = [[int(c) for c in li] for li in lines]

risk = 0
low_points = []
for j in range(len(grid)):
    for i in range(len(grid[j])):
        done = False
        search_coords = [
            x for x in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j))
            if x[0] >= 0 and x[0] < len(grid[j]) and x[1] >= 0
            and x[1] < len(grid)
        ]
        low_point = all(grid[x[1]][x[0]] > grid[j][i] for x in search_coords)
        if low_point:
            risk += grid[j][i] + 1
            low_points.append((i, j))

print("part a:", risk)

all_explored = set()
basins = []
for lp in low_points:
    if lp in all_explored:
        continue
    basin_size = 0
    to_explore = {lp}
    while len(to_explore) > 0:
        (i, j) = to_explore.pop()
        search_coords = [
            x for x in ((i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j))
            if x[0] >= 0 and x[0] < len(grid[j]) and x[1] >= 0
            and x[1] < len(grid)
        ]
        for s in search_coords:
            if s not in all_explored and grid[s[1]][s[0]] != 9:
                to_explore.add(s)
        all_explored.add((i, j))
        basin_size += 1
    basins.append(basin_size)

print("part b:", reduce(mul, sorted(basins, reverse=True)[:3], 1))
