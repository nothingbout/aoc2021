with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

risk_grid = []
for line in lines:
    risk_grid.append([int(x) for x in line])

grid_width = len(risk_grid[0])
grid_height = len(risk_grid)

min_risk_grid = [[None] * grid_width for _ in range(grid_height)]

def get_neighbor(x, y, n):
    if n == 0: return (x - 1, y) if x > 0 else None
    if n == 1: return (x, y - 1) if y > 0 else None
    if n == 2: return (x + 1, y) if x < grid_width - 1 else None
    if n == 3: return (x, y + 1) if y < grid_height - 1 else None

search_from = set([(0,0)])
min_risk_grid[0][0] = 0

while len(search_from) > 0:
    min_risk = None
    min_from = None

    for x, y in search_from:
        risk = min_risk_grid[y][x]
        if not min_risk or risk < min_risk:
            min_risk = risk
            min_from = (x, y)

    search_from.remove(min_from)

    from_x, from_y = min_from
    from_risk = min_risk_grid[from_y][from_x]
    for i in range(4):
        n = get_neighbor(from_x, from_y, i)
        if not n: continue

        nx, ny = n
        n_risk = from_risk + risk_grid[ny][nx]

        if not min_risk_grid[ny][nx] or n_risk < min_risk_grid[ny][nx]:
            min_risk_grid[ny][nx] = n_risk
            search_from.add((nx, ny))

print(min_risk_grid[-1][-1])