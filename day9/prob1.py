with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]


heightmap = []
for line in lines:
    row = [int(x) for x in line]
    heightmap.append(row)

width = len(heightmap[0])
height = len(heightmap)

def get_neighbor(x, y, n):
    if n == 0: return (x - 1, y) if x > 0 else None
    if n == 1: return (x, y - 1) if y > 0 else None
    if n == 2: return (x + 1, y) if x < width - 1 else None
    if n == 3: return (x, y + 1) if y < height - 1 else None

danger = 0

for y in range(height):
    for x in range(width):
        h = heightmap[y][x]

        lowest = True
        for n in range(4):
            neighbor = get_neighbor(x, y, n)
            if neighbor:
                (nx, ny) = neighbor
                if heightmap[ny][nx] <= h:
                    lowest = False
                    break

        if lowest:
            danger += h + 1

print(danger)
