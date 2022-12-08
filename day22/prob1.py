input_file = 'input.txt'

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point({self.x},{self.y},{self.z})'
    __repr__ = __str__

    def copy(self):
        return Point(self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z

    def add(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

class Cube:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self):
        return f'Cube({self.min},{self.max})'
    __repr__ = __str__

def parse_min_max(str):
    parts = str.split('..')
    return (int(parts[0][2:]), int(parts[1]))

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    ops_and_cubes = []
    for line in lines:
        op, cube_str = line.split()
        cube_parts = cube_str.split(',')
        x_min, x_max = parse_min_max(cube_parts[0])
        y_min, y_max = parse_min_max(cube_parts[1])
        z_min, z_max = parse_min_max(cube_parts[2])
        cube = Cube(Point(x_min, y_min, z_min), Point(x_max, y_max, z_max))
        ops_and_cubes.append((op, cube))
    return ops_and_cubes

class Reactor:
    def __init__(self, max_r):
        self.max_r = max_r
        self.cubes = []
        max_dim = 2 * max_r + 1
        for z in range(max_dim):
            plane = [] * (max_dim)
            for y in range(max_dim):
                plane.append([0] * (max_dim))
            self.cubes.append(plane)

    def index(self, point):
        return Point(point.x + self.max_r, point.y + self.max_r, point.z + self.max_r)

    def contains(self, point):
        if point.x < -self.max_r or point.x > self.max_r: return False
        if point.y < -self.max_r or point.y > self.max_r: return False
        if point.y < -self.max_r or point.z > self.max_r: return False
        return True

    def get(self, point):
        if not self.contains(point): return 0
        index = self.index(point)
        return self.cubes[index.z][index.y][index.x]

    def set(self, point, value):
        if not self.contains(point): return 0
        index = self.index(point)
        self.cubes[index.z][index.y][index.x] = value

    def constrain_cube(self, cube):
        m = cube.min
        m.x = max(-self.max_r, m.x)
        m.y = max(-self.max_r, m.y)
        m.z = max(-self.max_r, m.z)
        ma = cube.max
        ma.x = min(self.max_r, ma.x)
        ma.y = min(self.max_r, ma.y)
        ma.z = min(self.max_r, ma.z)
        return Cube(m, ma)

    def set_cube(self, cube, value):
        cube = self.constrain_cube(cube)
        for z in range(cube.min.z, cube.max.z + 1):
            for y in range(cube.min.y, cube.max.y + 1):
                for x in range(cube.min.x, cube.max.x + 1):
                    self.set(Point(x, y, z), value)

    def get_sum(self):
        total = 0
        for z in range(-self.max_r, self.max_r + 1):
            for y in range(-self.max_r, self.max_r + 1):
                total += sum(self.cubes[z][y])
        return total

ops_and_cubes = parse_input()
print(ops_and_cubes)

reactor = Reactor(50)

for op, cube in ops_and_cubes:
    value = 1 if op == "on" else 0
    reactor.set_cube(cube, value)

total_on = reactor.get_sum()
print(total_on)
