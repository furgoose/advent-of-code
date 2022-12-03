from aocd import lines


def priority(letter):
    return ord(letter) - 96 if ord(letter) > 96 else ord(letter) - 38


print(
    "part a:",
    sum(
        priority(x)
        for line in lines
        for x in set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
    ),
)

print(
    "part b:",
    sum(
        priority((set(a) & set(b) & set(c)).pop())
        for a, b, c in zip(lines[::3], lines[1::3], lines[2::3])
    ),
)
