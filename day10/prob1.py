with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

def get_closing(opening):
    if opening == '(': return ')'
    if opening == '[': return ']'
    if opening == '{': return '}'
    if opening == '<': return '>'

def get_score(closing):
    if closing == ')': return 3
    if closing == ']': return 57
    if closing == '}': return 1197
    if closing == '>': return 25137

total_score = 0

for line in lines:
    chunks = []
    for c in line:
        closing = get_closing(c)
        if closing:
            chunks.append(c)
        else:
            if get_closing(chunks.pop()) != c:
                total_score += get_score(c)

print(total_score)
