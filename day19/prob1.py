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

    def rotated_x(self, n):
        p = self
        for _ in range(n):
            p = Point(p.x, -p.z, p.y)
        return p

    def rotated_y(self, n):
        p = self
        for _ in range(n):
            p = Point(p.z, p.y, -p.x)
        return p

    def rotated_z(self, n):
        p = self
        for _ in range(n):
            p = Point(-p.y, p.x, p.z)
        return p

    def rotated(self, rotation):
        axis = rotation // 4
        n = rotation % 4
        match axis:
            case 0: # +X -> +X
                return self.rotated_x(n)
            case 1: # +X -> -X
                return self.rotated_z(2).rotated_x(n)
            case 2: # +X -> +Y
                return self.rotated_z(1).rotated_y(n)
            case 3: # +X -> -Y
                return self.rotated_z(3).rotated_y(n)
            case 4: # +X -> +Z
                return self.rotated_y(3).rotated_z(n)
            case 5: # +X -> -Z
                return self.rotated_y(1).rotated_z(n)

class Transform:
    def __init__(self, rotation, offset):
        self.rotation = rotation
        self.offset = offset

    def __str__(self):
        return f'Transform({self.rotation},{self.offset})'
    __repr__ = __str__
 

class Scanner:
    def __init__(self, beacons):
        self.beacons = beacons

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    scanners = []
    current_scanner_beacons = []
    for line in lines:
        if len(line) == 0: continue
        if line.startswith('--- scanner'):
            if len(current_scanner_beacons) > 0: scanners.append(Scanner(current_scanner_beacons))
            current_scanner_beacons = []
            continue

        (x, y, z) = [int(a) for a in line.split(',')]
        current_scanner_beacons.append(Point(x, y, z))

    scanners.append(Scanner(current_scanner_beacons))
    return scanners

def is_overlap(a_beacons, b_beacons):
    return len(set(a_beacons).intersection(b_beacons)) >= 12

def rotate_beacons(beacons, rotation):
    return [p.rotated(rotation) for p in beacons]

def offset_beacons(beacons, offset):
    return [p.add(offset) for p in beacons]

def transform_beacons(beacons, transform):
    return offset_beacons(rotate_beacons(beacons, transform.rotation), transform.offset)

def find_overlap(scanner_a, scanner_b, a_transform):
    a_beacons = transform_beacons(scanner_a.beacons, a_transform)

    for rotation in range(24):
        b_beacons = rotate_beacons(scanner_b.beacons, rotation)

        for p1 in a_beacons:
            for p2 in b_beacons:
                offset = p1.sub(p2)
                if is_overlap(a_beacons, offset_beacons(b_beacons, offset)):
                    # print(f'overlap: {rotation} {offset}')
                    return Transform(rotation, offset)


scanners = parse_input()
scanner_transforms = [None] * len(scanners)
scanner_transforms[0] = Transform(0, Point(0, 0, 0))

while None in scanner_transforms:
    for a_index in range(len(scanners)):
        a_transform = scanner_transforms[a_index]
        if a_transform is None: continue

        for b_index in range(len(scanners)):
            if scanner_transforms[b_index] is not None: continue

            transform = find_overlap(scanners[a_index], scanners[b_index], a_transform)
            if transform:
                scanner_transforms[b_index] = transform
                print(f'overlap: {a_index}-{b_index}, rotation: {transform.rotation}, offset: {transform.offset}')
                break

all_beacons = set()
for i in range(len(scanners)):
    beacons = transform_beacons(scanners[i].beacons, scanner_transforms[i])
    all_beacons = all_beacons.union(set(beacons))

print(len(all_beacons))