with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

for line in lines:
    positions = sorted([int(x) for x in line.split(',')])

    distance_costs = [0]
    for d in range(1, positions[-1] - positions[0] + 1):
        distance_costs.append(distance_costs[d - 1] + d)

    min_target = -1
    min_cost = -1

    for target in range(positions[0], positions[-1] + 1):
        cost = sum([distance_costs[abs(p - target)] for p in positions])
        # print(f'target: {target}, cost: {cost}')

        if min_cost < 0 or cost < min_cost:
            min_cost = cost
            min_target = target

    print(min_cost)

