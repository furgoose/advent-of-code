from aocd import lines
from copy import deepcopy

grid = [[int(n) for n in line] for line in lines]


def step(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
    increased = True
    flashed = set()
    while increased:
        increased = False
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    search_coords = [
                        x for x in (
                            (x - 1, y - 1),
                            (x, y - 1),
                            (x + 1, y - 1),
                            (x - 1, y),
                            (x + 1, y),
                            (x - 1, y + 1),
                            (x, y + 1),
                            (x + 1, y + 1),
                        ) if x[0] >= 0 and x[0] < len(grid[y]) and x[1] >= 0
                        and x[1] < len(grid)
                    ]
                    for cx, cy in search_coords:
                        grid[cy][cx] += 1
                    increased = True
    for x, y in flashed:
        grid[y][x] = 0
    return len(flashed)


grid_a = deepcopy(grid)
print("part a:", sum(step(grid_a) for _ in range(100)))

flashes_this_step = 0
steps = 0
while flashes_this_step != len(grid) * len(grid[0]):
    flashes_this_step = step(grid)
    steps += 1
print("part b:", steps)
