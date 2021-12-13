from aocd import lines

input = [x.strip() for x in lines]

str_length = len(input[0])
lines = len(input)

bits = [0] * str_length
for i in range(lines):
    for j in range(len(input[i])):
        bits[j] += int(input[i][j])

bits = "".join("01"[bits[j] > lines / 2] for j in range(str_length))
gamma = int(bits, 2)
epsilon = gamma ^ int("1" * str_length, 2)
print("part a:", gamma * epsilon)


def find_most_common(input, place):
    ones = [x[place] for x in input if x[place] == "1"]
    return 1 if len(ones) >= (len(input) / 2) else 0


oxy = input
for b in range(str_length):
    if len(oxy) <= 1:
        break
    oxy = [x for x in oxy if int(x[b]) == find_most_common(oxy, b)]
co2 = input
for b in range(str_length):
    if len(co2) <= 1:
        break
    co2 = [x for x in co2 if int(x[b]) == (find_most_common(co2, b) ^ 1)]

print("part b:", int(oxy[0], 2) * int(co2[0], 2))
