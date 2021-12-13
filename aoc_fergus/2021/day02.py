from aocd import lines

report = [x.strip().split() for x in lines]

pos = 0
depth_a = depth_b = 0
aim = 0
for (i, j) in report:
    j = int(j)
    if i == "forward":
        pos += j
        depth_b += aim * j
    if i == "down":
        depth_a += j
        aim += j
    if i == "up":
        depth_a -= j
        aim -= j
print("part 1:", pos * depth_a)
print("part 2:", pos * depth_b)
