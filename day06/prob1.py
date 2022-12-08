with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

for line in lines:
    timers = [int(x) for x in line.split(',')]

    for _ in range(80):
        count = len(timers)

        for i in range(count):
            if timers[i] == 0:
                timers[i] = 6
                timers.append(8)
            else:
                timers[i] -= 1

    print(len(timers))