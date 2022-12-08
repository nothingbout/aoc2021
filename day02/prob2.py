with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

pos = 0
depth = 0
aim = 0

for line in lines:
    cols = line.split()
    value = int(cols[1])

    if cols[0] == 'forward':
        pos += value
        depth += value * aim
    elif cols[0] == 'down':
        aim += value
    elif cols[0] == 'up':
        aim -= value

print(pos * depth)