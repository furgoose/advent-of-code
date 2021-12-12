from aocd import lines

from collections import defaultdict

edges = defaultdict(set)
for line in lines:
    a, b = line.split("-")
    edges[a].add(b)
    edges[b].add(a)


def dfs(start, seen, part_b=False):
    if start == "end":
        return 1

    paths = 0
    for end in edges[start]:
        if end not in seen:
            new_seen = seen.copy()
            if end.islower():
                new_seen.add(end)
            paths += dfs(end, new_seen, part_b)
        elif part_b and end != "start":
            paths += dfs(end, seen, False)

    return paths


print("part a:", dfs("start", {"start"}))
print("part b:", dfs("start", {"start"}, True))
