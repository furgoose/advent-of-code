from aocd import data

offset = 0
while len(set(data[offset : offset + 4])) != 4:
    offset += 1

print("part a:", offset + 4)

offset = 0
while len(set(data[offset : offset + 14])) != 14:
    offset += 1

print("part b:", offset + 14)
