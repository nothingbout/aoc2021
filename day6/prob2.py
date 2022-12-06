with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

for line in lines:
    start_timers = [int(x) for x in line.split(',')]
    count_by_timer = [0] * 9
    for timer in start_timers: count_by_timer[timer] += 1

    for _ in range(256):
        zero_count = count_by_timer[0]
        for i in range(0, len(count_by_timer) - 1):
            count_by_timer[i] = count_by_timer[i + 1]

        count_by_timer[6] += zero_count
        count_by_timer[8] = zero_count

    print(sum(count_by_timer))