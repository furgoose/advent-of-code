from copy import deepcopy
from aocd import lines


lines = iter(lines)
rows = []
line = next(lines)
while "[" in line:
    rows.append([line[i] for i in range(1, len(line), 4)])
    line = next(lines)
# Read in all the rows of crates
stacks = [[] for _ in range(len(rows[0]))]
for row in rows[::-1]:
    for index, crate in enumerate(row):
        if crate != " ":
            stacks[index].append(crate)
stacks_b = deepcopy(stacks)

# Skip blank line
next(lines)

# Process instructions
for line in lines:
    _, amount, _, from_stack, _, to_stack = line.split()
    amount, from_stack, to_stack = int(amount), int(from_stack) - 1, int(to_stack) - 1
    for i in range(amount):
        stacks[to_stack].append(stacks[from_stack].pop())
    stacks_b[to_stack].extend(stacks_b[from_stack][-amount:])
    stacks_b[from_stack] = stacks_b[from_stack][:-amount]


print("part a:", "".join(stack[-1] for stack in stacks))
print("part b:", "".join(stack[-1] for stack in stacks_b))
