with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

polymer = lines[0]

rules = []
for line in lines[2:]:
    rule = line.split(' -> ')
    rules.append(rule)

# print(polymer)
# print(rules)

pair_counts = {}
for i in range(len(polymer) - 1):
    pair = polymer[i:i+2]
    pair_counts[pair] = pair_counts.get(pair, 0) + 1

counts = {}
for c in polymer:
    counts[c] = counts.get(c, 0) +  1

for _ in range(40):
    new_pair_counts = pair_counts.copy()
    for rule in rules:
        if not rule[0] in pair_counts: continue

        count = pair_counts[rule[0]]

        new_pair1 = rule[0][0] + rule[1]
        if not new_pair1 in new_pair_counts: new_pair_counts[new_pair1] = 0

        new_pair2 = rule[1] + rule[0][1]
        if not new_pair2 in new_pair_counts: new_pair_counts[new_pair2] = 0

        new_pair_counts[rule[0]] -= count
        new_pair_counts[new_pair1] = new_pair_counts.get(new_pair1, 0) + count
        new_pair_counts[new_pair2] = new_pair_counts.get(new_pair2, 0) + count

        counts[rule[1]] = counts.get(rule[1], 0) + count

    pair_counts = new_pair_counts


# print(pair_counts)
# print(counts)

counts = list(zip(counts.keys(), counts.values()))
counts = sorted(counts, key=lambda x: x[1])
# print(counts)
print(counts[-1][1] - counts[0][1])
