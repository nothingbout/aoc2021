input_file = 'input.txt'

class Grid:
    def __init__(self, rows):
        self.rows = rows
        self.width = len(rows[0])
        self.height = len(rows)

    def copy(self):
        return Grid([row.copy() for row in self.rows])

    def print(self):
        for row in self.rows:
            print(''.join(row))
        print('')

    def wrap(self, x, y):
        if x >= self.width: x -= self.width
        if y >= self.height: y -= self.height
        return (x, y)

    def empty(self, x, y):
        return self.get(x, y) == '.'

    def get(self, x, y):
        x, y = self.wrap(x, y)
        return self.rows[y][x]

    def set(self, x, y, value):
        x, y = self.wrap(x, y)
        self.rows[y][x] = value

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]


    rows = []
    for line in lines:
        rows.append([x for x in line])

    return Grid(rows)

def simulate(grid):
    moved = False

    new_grid = grid.copy()
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == '>':
                if grid.empty(x + 1, y):
                    moved = True
                    new_grid.set(x, y, '.')
                    new_grid.set(x + 1, y, '>')

    grid = new_grid
    new_grid = grid.copy()

    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) == 'v':
                if grid.empty(x, y + 1):
                    moved = True
                    new_grid.set(x, y, '.')
                    new_grid.set(x, y + 1, 'v')

    return (new_grid, moved)

grid = parse_input()
grid.print()

step = 0
while True:
    grid, moved = simulate(grid)
    step += 1
    print(step)
    # grid.print()
    if not moved:
        break
