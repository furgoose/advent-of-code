from aocd import numbers as ns

print("part a:", sum(n2 > n1 for n1, n2 in zip(ns, ns[1:])))
print("part b:", sum(n2 > n1 for n1, n2 in zip(ns, ns[3:])))
