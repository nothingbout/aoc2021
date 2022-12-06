from functools import reduce

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]


heightmap = []
for line in lines:
    row = [int(x) for x in line]
    heightmap.append(row)

width = len(heightmap[0])
height = len(heightmap)

searched = [[False] * width for _ in range(height)]

def get_neighbor(x, y, n):
    if n == 0: return (x - 1, y) if x > 0 else None
    if n == 1: return (x, y - 1) if y > 0 else None
    if n == 2: return (x + 1, y) if x < width - 1 else None
    if n == 3: return (x, y + 1) if y < height - 1 else None

def basin_size(x, y):
    if searched[y][x] or heightmap[y][x] == 9: return 0

    searched[y][x] = True

    size = 1
    for i in range(4):
        n = get_neighbor(x, y, i)
        if not n: continue
        size += basin_size(n[0], n[1])

    return size


basin_sizes = []

for y in range(height):
    for x in range(width):
        if searched[y][x]: continue

        size = basin_size(x, y)
        basin_sizes.append(size)

top_sizes = sorted(basin_sizes)[-3:]
total = reduce(lambda x, y: x * y, top_sizes)

print(total)
