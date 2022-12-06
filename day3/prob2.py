def most_common(b, lines):
    one_count = 0
    zero_count = 0
    for line in lines:
        if line[b] == '1': one_count += 1
        else: zero_count += 1
    if one_count > zero_count: return '1'
    if zero_count > one_count: return '0'
    return None

def make_num(line):
    num = 0
    for b in range(len(line)):
        num <<= 1
        if line[b] == '1': num |= 1
    return num

with open('input.txt', 'r') as f:
    all_lines = [line.rstrip('\r\n') for line in f.readlines()]

num_bits = len(all_lines[0])

oxygen_lines = all_lines
for b in range(num_bits):
    x = most_common(b, oxygen_lines)
    if not x: x = '1'
    oxygen_lines = list(filter(lambda line: line[b] == x, oxygen_lines))
    if len(oxygen_lines) <= 1: break

co2_lines = all_lines
for b in range(num_bits):
    x = most_common(b, co2_lines)
    if not x: x = '1'
    co2_lines = list(filter(lambda line: line[b] != x, co2_lines))
    if len(co2_lines) <= 1: break

# print(oxygen_lines[0])
# print(co2_lines[0])

print(make_num(oxygen_lines[0]) * make_num(co2_lines[0]))
