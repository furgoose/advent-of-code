from aocd import lines

grid = []
width = height = 0
line = lines.pop(0)
while line != "":
    x, y = [int(i) for i in line.split(",")]
    if x + 1 > width:
        for l in grid:
            l += ["."] * (x + 1 - width)
        width = x + 1
    if y + 1 > height:
        grid += [["."] * width for _ in range(y + 1 - height)]
        height = y + 1
    grid[y][x] = "#"
    line = lines.pop(0)

first_fold = True
for fold in lines:
    d, a = fold[11:].split("=")
    a = int(a)
    if d == "y":
        part_a = grid[:a]
        part_b = grid[(a + 1):]
        for i in range(len(part_b)):
            for c in range(len(part_b[i])):
                if part_b[i][c] == "#":
                    part_a[a - i - 1][c] = "#"
        grid = part_a
    if d == "x":
        for i in range(len(grid)):
            part_a = grid[i][:a]
            part_b = grid[i][(a + 1):]
            for c in range(len(part_b)):
                if part_b[c] == "#":
                    part_a[a - c - 1] = "#"
            grid[i] = part_a
    if first_fold:
        print("part a:", sum(x == "#" for l in grid for x in l))
        first_fold = False

# I know this won't work unless you have the same code as me but I'm not figuring out all the letters
alphabet = {
    ".##.#..##..######..##..#": "A",
    "###.#..####.#..##..####.": "B",
    ".##.#..##...#...#..#.##.": "C",
    "#####...###.#...#...####": "E",
    "#####...###.#...#...#...": "F",
    ".##.#..##...#.###..#.###": "G",
    "#..##..######..##..##..#": "H",
    "..##...#...#...##..#.##.": "J",
    "#..##.#.##..#.#.#.#.#..#": "K",
    "#...#...#...#...#...####": "L",
    "###.#..##..####.#.#.#..#": "R",
    "#..##..##..##..##..#.##.": "U",
    "####...#..#..#..#...####": "Z",
}

letters = [""] * 8
for line in grid:
    ls = ["".join(line[i:i + 4]) for i in range(0, len(line), 5)]
    for i in range(8):
        letters[i] += ls[i]
print("part b:", "".join(alphabet[i] for i in letters))
