from aocd import lines


def bitrange(i, j):
    res = 0
    for x in range(min(i, j), max(i, j) + 1):
        res |= 1 << x
    return res


overlapping_complete = 0
overlapping_partial = 0
for line in lines:
    a1, a2, b1, b2 = [int(x) for elf in line.split(",") for x in elf.split("-")]
    a = bitrange(a1, a2)
    b = bitrange(b1, b2)
    if a & b in [a, b]:
        overlapping_complete += 1
    if a & b != 0:
        overlapping_partial += 1

print("part a:", overlapping_complete)
print("part b:", overlapping_partial)
