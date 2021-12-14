from aocd import lines
from collections import Counter

template = lines.pop(0)
rules = dict(line.split(" -> ") for line in lines[1:])

pairs = Counter(x + y for x, y in zip(template, template[1:]))
counts = Counter(template)
for step in range(40):
    if step == 10:
        com = counts.most_common()
        print("part a:", com[0][1] - com[-1][1])
    new_pairs = Counter()
    for p, n in pairs.items():
        new_pairs[p[0] + rules[p]] += n
        new_pairs[rules[p] + p[1]] += n
        counts += {rules[p]: n}
    pairs = new_pairs

com = counts.most_common()
print("part b:", com[0][1] - com[-1][1])
