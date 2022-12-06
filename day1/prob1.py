with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

prev = None
increased_count = 0

for line in lines:
    value = int(line)
    if prev:
        if value > prev:
            increased_count += 1
    prev = value

print(increased_count)
