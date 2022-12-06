with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

grid = []
for line in lines:
    row = [int(x) for x in line]
    grid.append(row)

width = len(grid[0])
height = len(grid)

flashed = [[False] * width for _ in range(height)]

def get_neighbor_unchecked(x, y, n):
    if n == 0: return (x + 1, y)
    if n == 1: return (x + 1, y + 1)
    if n == 2: return (x, y + 1)
    if n == 3: return (x - 1, y + 1)
    if n == 4: return (x - 1, y)
    if n == 5: return (x - 1, y -1)
    if n == 6: return (x, y - 1)
    if n == 7: return (x + 1, y - 1)

def get_neighbor(x, y, n):
    (nx, ny) = get_neighbor_unchecked(x, y, n)
    if nx < 0 or nx >= width: return None
    if ny < 0 or ny >= height: return None
    return (nx, ny)

def maybe_flash(x, y):
    if flashed[y][x] or grid[y][x] < 10: return 0
    flashed[y][x] = True

    count = 1
    for i in range(8):
        n = get_neighbor(x, y, i)
        if not n: continue
        nx, ny = n
        grid[ny][nx] += 1
        count += maybe_flash(nx, ny)

    return count

total_flashes = 0

for step in range(10000):
    for x in range(width):
        for y in range(height):
            grid[y][x] += 1

    flashes = 0
    for x in range(width):
        for y in range(height):
            flashes += maybe_flash(x, y)

    total_flashes += flashes
    if flashes == width * height:
        print(step + 1)
        break

    for x in range(width):
        for y in range(height):
            if flashed[y][x]:
                flashed[y][x] = False
                grid[y][x] = 0


# print(total_flashes)

    