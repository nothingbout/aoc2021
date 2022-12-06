with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

num_bits = len(lines[0])
gamma = 0
epsilon = 0

for b in range(num_bits):
    one_count = 0
    zero_count = 0

    for line in lines:
        if line[b] == '1': one_count += 1
        else: zero_count += 1

    gamma <<= 1
    epsilon <<= 1
    if one_count > zero_count: gamma |= 1
    else: epsilon |= 1

print(gamma * epsilon)