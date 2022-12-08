with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

count = 0

for line in lines:
    parts = line.split(' | ')
    signals = parts[0].split()
    outputs = parts[1].split()

    for output in outputs:
        l = len(output)
        if l == 2 or l == 3 or l == 4 or l == 7:
            count += 1

print(count)
