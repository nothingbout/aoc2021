input_file = 'example_input.txt'

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    for line in lines:
        print(line)

    return lines
