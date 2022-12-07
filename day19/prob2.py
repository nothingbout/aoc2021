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

input_points = [
    Point(0,0,0),
    Point(-1224,129,-75),
    Point(-1195,1306,-26),
    Point(-1301,1160,1257),
    Point(-1315,-1101,-76),
    Point(-1187,2418,1161),
    Point(-2467,1223,-47),
    Point(-1270,2426,2430),
    Point(-1290,2405,3588),
    Point(-3684,1322,75),
    Point(-1215,2542,31),
    Point(-3587,2513,-104),
    Point(-2452,1184,-1288),
    Point(-1342,2346,-1176),
    Point(-3757,3636,29),
    Point(-4878,3698,-105),
    Point(-1273,3668,-1161),
    Point(-4961,3567,-1140),
    Point(-3754,3674,-1246),
    Point(-2371,1314,-2479),
    Point(-3688,2399,-1283),
    Point(-71,2457,-92),
    Point(-2495,3697,-1224),
    Point(-2547,3702,-53),
    Point(-85,2423,-1263),
    Point(-4854,2399,-1178),
    Point(1120,2436,-1288),
    Point(-1244,3647,-74),
    Point(-2538,3721,1107)
]

def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z)

max_distance = 0
for a in input_points:
    for b in input_points:
        max_distance = max(max_distance, manhattan(a, b))

print(max_distance)