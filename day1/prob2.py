with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

prev = None
increased_count = 0

for i in range(2, len(lines)):
    value = sum(map(int, lines[i - 2:i + 1]))
    if prev:
        if value > prev:
            increased_count += 1
    prev = value

print(increased_count)
