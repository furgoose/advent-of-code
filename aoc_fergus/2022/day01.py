from aocd import data

calories = sorted(sum(int(i) for i in elf.split("\n")) for elf in data.split("\n\n"))
print("part a:", calories[-1])
print("part b:", sum(calories[-3:]))
