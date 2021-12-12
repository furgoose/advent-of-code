from aocd import data
from collections import defaultdict, Counter


def solution(fish, days):
    for _ in range(days):
        new_fish = defaultdict(int)

        for t, n in fish.items():
            t -= 1
            if t < 0:
                new_fish[6] += n
                new_fish[8] += n
            else:
                new_fish[t] += n
        fish = new_fish

    return sum(fish.values())


input = Counter(map(int, data.split(",")))
print(solution(input.copy(), 80))
print(solution(input.copy(), 256))
