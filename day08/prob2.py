with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

def find_and_remove(all_values, digit, function):
    values = list(filter(function, all_values))
    if len(values) != 1:
        print(f"Unexpected number of values for {digit}: {len(values)}")
    value = values[0]
    all_values.remove(value)
    return value

def num_common(a, b):
    return len(set(a).intersection(set(b)))

total_sum = 0

for line in lines:
    parts = line.split(' | ')
    signals = [''.join(sorted(s)) for s in parts[0].split()]
    outputs = [''.join(sorted(s)) for s in parts[1].split()]

    # print(signals)
    # print(outputs)

    digits = [None] * 10
    digits[1] = find_and_remove(signals, 1, lambda s: len(s) == 2)
    digits[4] = find_and_remove(signals, 4, lambda s: len(s) == 4)
    digits[7] = find_and_remove(signals, 7, lambda s: len(s) == 3)
    digits[8] = find_and_remove(signals, 8, lambda s: len(s) == 7)

    digits[3] = find_and_remove(signals, 3, lambda s: len(s) == 5 and num_common(s, digits[1]) == 2)
    digits[5] = find_and_remove(signals, 5, lambda s: len(s) == 5 and num_common(s, digits[4]) == 3)
    digits[2] = find_and_remove(signals, 2, lambda s: len(s) == 5)

    digits[9] = find_and_remove(signals, 9, lambda s: len(s) == 6 and num_common(s, digits[3]) == 5)
    digits[6] = find_and_remove(signals, 6, lambda s: len(s) == 6 and num_common(s, digits[5]) == 5)
    digits[0] = find_and_remove(signals, 0, lambda s: len(s) == 6)

    # print(digits)
    # print(signals)

    output_num = 0
    for output in outputs:
        output_num *= 10
        output_num += digits.index(output)

    # print(output_num)
    total_sum += output_num

print(total_sum)
