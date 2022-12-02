from aocd import lines

normalised = [(ord(a) - 64, ord(b) - 87) for line in lines for a, b in [line.split()]]
winner = {1: 2, 2: 3, 3: 1}
loser = {b: a for a, b in winner.items()}

print(
    "part a:",
    sum(b + 6 if winner[a] == b else b + 3 if a == b else b for a, b in normalised),
)
print(
    "part b:",
    sum(
        winner[a] + 6 if b == 3 else loser[a] if b == 1 else a + 3
        for a, b in normalised
    ),
)
