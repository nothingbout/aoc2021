with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

def get_closing(opening):
    if opening == '(': return ')'
    if opening == '[': return ']'
    if opening == '{': return '}'
    if opening == '<': return '>'

def get_score(closing):
    if closing == ')': return 1
    if closing == ']': return 2
    if closing == '}': return 3
    if closing == '>': return 4

scores = []

for line in lines:
    chunks = []
    corrupted = False
    for c in line:
        closing = get_closing(c)
        if closing:
            chunks.append(c)
        else:
            if get_closing(chunks.pop()) != c:
                corrupted = True

    score = 0
    if not corrupted:
        for c in reversed(chunks):
            score *= 5
            score += get_score(get_closing(c))

        scores.append(score)

scores = sorted(scores)
print(scores[(len(scores) // 2)])
