with open('example_input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

for line in lines:
    print(line)

