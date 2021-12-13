from aocd import data


def solution1(input):
    lines = []
    max_x = 0
    max_y = 0
    for l in input:
        p1, p2 = [[int(x) for x in i.split(",")] for i in l.split(" -> ")]
        lines.append((p1, p2))
        max_x = max(max_x, p1[0], p2[0])
        max_y = max(max_y, p1[1], p2[1])
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (p1, p2) in lines:
        if p1[0] == p2[0] or p1[1] == p2[1]:
            x1, x2 = sorted([p1[0], p2[0]])
            y1, y2 = sorted([p1[1], p2[1]])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[y][x] += 1
    return sum(sum(1 if x >= 2 else 0 for x in l) for l in grid)


def solution2(input):
    lines = []
    max_x = 0
    max_y = 0
    for l in input:
        p1, p2 = [[int(x) for x in i.split(",")] for i in l.split(" -> ")]
        lines.append((p1, p2))
        max_x = max(max_x, p1[0], p2[0])
        max_y = max(max_y, p1[1], p2[1])
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (p1, p2) in lines:
        if p1[0] == p2[0] or p1[1] == p2[1]:
            x1, x2 = sorted([p1[0], p2[0]])
            y1, y2 = sorted([p1[1], p2[1]])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[y][x] += 1
        else:
            x_step = -1 if p2[0] < p1[0] else 1
            y_step = -1 if p2[1] < p1[1] else 1
            for x, y in zip(
                    range(p1[0], p2[0] + x_step, x_step),
                    range(p1[1], p2[1] + y_step, y_step),
            ):
                print(x, y)
                grid[y][x] += 1
    return sum(sum(1 if x >= 2 else 0 for x in l) for l in grid)


input = [x.strip() for x in data.splitlines()]

print("part a:", solution1(input))
print("part b:", solution2(input))
