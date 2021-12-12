from collections import defaultdict
from aocd import lines

r1478 = 0
total = 0
for entry in lines:
    signals, output = [x.split() for x in entry.split(" | ")]
    patterns = defaultdict(list)
    for s in signals:
        patterns.setdefault(len(s), []).append(set(s))
    one = patterns[2].pop()
    four = patterns[4].pop()
    seven = patterns[3].pop()
    eight = patterns[7].pop()

    for p in range(len(patterns[6])):
        if len(patterns[6][p] - seven - four) == 1:
            break
    nine = patterns[6].pop(p)

    seg_dc = patterns[6][0] ^ patterns[6][1]
    seg_d = seg_dc - one

    seg_a = seven - one
    seg_b = four - one - seg_d
    seg_c = seg_dc - seg_d
    seg_e = eight - nine
    seg_f = seven - seg_a - seg_c

    six = eight - seg_c
    five = six - seg_e
    three = nine - seg_b
    two = eight - seg_b - seg_f
    zero = eight - seg_d

    r = ""
    for v in output:
        v = set(v)
        if v == zero:
            r += "0"
        if v == one:
            r1478 += 1
            r += "1"
        elif v == two:
            r += "2"
        elif v == three:
            r += "3"
        elif v == four:
            r1478 += 1
            r += "4"
        elif v == five:
            r += "5"
        elif v == six:
            r += "6"
        elif v == seven:
            r += "7"
            r1478 += 1
        elif v == eight:
            r += "8"
            r1478 += 1
        elif v == nine:
            r += "9"
    total += int(r)


print("part a:", r1478)
print("part b:", total)
