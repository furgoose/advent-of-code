from aocd import lines
import heapq

m = [[int(c) for c in l] for l in lines]


def aStar(g, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    grid_height = len(g)
    grid_width = len(g[0])

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        x, y = current
        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        neighbors = filter(
            lambda x: 0 <= x[0] < grid_width and 0 <= x[1] < grid_height,
            neighbors)
        for next_node in neighbors:
            new_cost = cost_so_far[current] + g[next_node[1]][next_node[0]]
            if next_node not in cost_so_far or new_cost < cost_so_far[
                    next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + abs(next_node[0] -
                                          goal[0]) + abs(next_node[1] -
                                                         goal[1])
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current

    return came_from, cost_so_far


u = (len(m[0]) - 1, len(m) - 1)
came_from, cost_so_far = aStar(m, (0, 0), u)
print("part a:", cost_so_far[u])

expanded_grid = [[] for _ in range(5 * len(m))]

for y in range(5):
    for x in range(5):
        for i in range(len(m)):
            expanded_grid[len(m) * y + i] += [(j + x + y - 1) % 9 + 1
                                              for j in m[i]]

u = (len(expanded_grid[0]) - 1, len(expanded_grid) - 1)
came_from, cost_so_far = aStar(expanded_grid, (0, 0), u)
print("part b:", cost_so_far[u])
