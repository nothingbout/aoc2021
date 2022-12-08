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

    def min(self, other):
        return Point(min(self.x, other.x), min(self.y, other.y), min(self.z, other.z))

    def max(self, other):
        return Point(max(self.x, other.x), max(self.y, other.y), max(self.z, other.z))

class Cube:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __str__(self):
        return f'Cube({self.min},{self.max})'
    __repr__ = __str__

    def intersection(self, cube):
        new_min = self.min.max(cube.min)
        new_max = self.max.min(cube.max)
        if new_min.x > new_max.x: return None
        if new_min.y > new_max.y: return None
        if new_min.z > new_max.z: return None
        return Cube(new_min, new_max)

    def size(self):
        return self.max.sub(self.min).add(Point(1, 1, 1))

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
    def __init__(self):
        self.plus_cubes = []
        self.minus_cubes = []

    def set_cube(self, cube, value):
        new_minus_cubes = []
        for other in self.plus_cubes:
            intersection = cube.intersection(other)
            if intersection: new_minus_cubes.append(intersection)

        new_plus_cubes = []
        for other in self.minus_cubes:
            intersection = cube.intersection(other)
            if intersection: new_plus_cubes.append(intersection)

        self.minus_cubes.extend(new_minus_cubes)
        self.plus_cubes.extend(new_plus_cubes)

        if value > 0:
            self.plus_cubes.append(cube)

    def get_sum(self):
        total = 0
        for cube in self.plus_cubes:
            size = cube.size()
            total += size.x * size.y * size.z

        for cube in self.minus_cubes:
            size = cube.size()
            total -= size.x * size.y * size.z
        return total

ops_and_cubes = parse_input()
# print(ops_and_cubes)

reactor = Reactor()

for op, cube in ops_and_cubes:
    value = 1 if op == "on" else 0
    reactor.set_cube(cube, value)

total_on = reactor.get_sum()
print(total_on)
