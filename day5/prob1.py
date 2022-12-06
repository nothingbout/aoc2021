with open('input.txt', 'r') as f:
    input_lines = [line.rstrip('\r\n') for line in f.readlines()]

segments = []
for line in input_lines:
    point_strs = line.split(' -> ')
    points = []
    for str in point_strs:
        point = tuple([int(x) for x in str.split(',')])
        points.append(point)
    segments.append(tuple(points))

max_x = 0
max_y = 0
for segment in segments:
    for point in segment:
        if point[0] > max_x: max_x = point[0]
        if point[1] > max_y: max_y = point[1]

grid_w = max_x + 1
grid_h = max_y + 1
grid = [[0] * grid_w for _ in range(grid_h)]

def get_delta(start, end):
    if end < start: return -1
    if end > start: return 1
    return 0

def draw_segment(grid, start_point, end_point):
    (x, y) = start_point
    (end_x, end_y) = end_point
    x_delta = get_delta(x, end_x)
    y_delta = get_delta(y, end_y)

    new_overlaps = 0

    while x != end_x or y != end_y:
        if grid[y][x] == 1: new_overlaps += 1
        grid[y][x] += 1
        x += x_delta
        y += y_delta

    if grid[y][x] == 1: new_overlaps += 1
    grid[y][x] += 1

    return new_overlaps

# print(grid)
overlaps = 0
for segment in segments:
    if segment[0][0] != segment[1][0] and segment[0][1] != segment[1][1]: continue
    # print(segment)
    overlaps += draw_segment(grid, segment[0], segment[1])
    # print(grid)

# print(grid)
print(overlaps)