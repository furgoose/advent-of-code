from aocd import lines
import re

total = 0
for line in lines:
    m = re.findall(r"\d", line)
    total += int(m[0] + m[-1])
print(total)


total2 = 0
for line in lines:
    line = (
        line.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "4")
        .replace("five", "5e")
        .replace("six", "6")
        .replace("seven", "7n")
        .replace("eight", "e8t")
        .replace("nine", "9e")
    )
    m = re.findall(r"\d", line)
    total2 += int(m[0] + m[-1])
print(total2)
