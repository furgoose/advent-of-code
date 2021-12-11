from aocd import lines

mapping = {"(": ")", "[": "]", "{": "}", "<": ">"}
invalid_score_map = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete_score_map = {")": 1, "]": 2, "}": 3, ">": 4}
total_error = 0
complete_scores = []

for line in lines:
    valid = True
    expected = []
    for c in line:
        if c in mapping.keys():
            expected.append(mapping[c])
        elif c != expected[-1]:
            valid = False
            break
        else:
            expected = expected[:-1]
    if not valid:
        total_error += invalid_score_map[c]
    else:
        score = 0
        for c in expected[::-1]:
            score *= 5
            score += complete_score_map[c]
        complete_scores.append(score)


print("part a:", total_error)
print("part b:", sorted(complete_scores)[int((len(complete_scores) - 1) / 2)])
