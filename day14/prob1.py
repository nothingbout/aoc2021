with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

polymer = lines[0]

rules = {}
for line in lines[2:]:
    rule = line.split(' -> ')
    rules[rule[0]] = rule[1]

# print(polymer)
# print(rules)

for _ in range(10):
    i = 0
    while i < len(polymer) - 1:
        rule = rules.get(polymer[i:i+2], None)
        if rule:
            polymer = polymer[:i + 1] + rule + polymer[i + 1:]
            i += 1
        i += 1

# print(polymer)

counts = {}
for c in polymer:
    if not c in counts:
        counts[c] = 0
    counts[c] += 1

counts = list(zip(counts.keys(), counts.values()))
counts = sorted(counts, key=lambda x: x[1])
# print(counts)
print(counts[-1][1] - counts[0][1])
