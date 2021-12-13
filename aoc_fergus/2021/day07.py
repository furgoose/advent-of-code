from aocd import data

ns = [int(n) for n in data.split(",")]
max_n = max(ns)

dist_to_pos = [[abs(n - pos) for n in ns] for pos in range(max_n)]

print("part a:", min(sum(pos) for pos in dist_to_pos))
print("part b:",
      min(sum(int(n * (n + 1) / 2) for n in pos) for pos in dist_to_pos))
