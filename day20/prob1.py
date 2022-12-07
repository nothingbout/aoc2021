input_file = 'example_input.txt'

class Image:
    def __init__(self, rows):
        self.rows = rows
        self.width = len(rows[0])
        self.height = len(rows[1])

    def print(self):
        for row in self.rows:
            print(row)

    def is_lit(self, x, y, void_is_lit):
        if x < 0 or x >= self.width: return void_is_lit
        if y < 0 or y >= self.height: return void_is_lit
        if self.rows[y][x] == '#': return True
        if self.rows[y][x] != '.': raise "wut"
        return False

    def get_square_value(self, x, y, void_is_lit, max_offset = 1):
        value = 0
        for dy in range(-max_offset, max_offset + 1):
            for dx in range(-max_offset, max_offset + 1):
                value <<= 1
                if self.is_lit(x + dx, y + dy, void_is_lit):
                    value |= 1
        return value

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]
    return (lines[0], Image(lines[2:]))

def enhance(input_image, algorithm, iteration):
    void_is_lit = False
    if algorithm[0] == '#' and algorithm[-1] == '.':
        void_is_lit = iteration % 2 == 1

    expansion = 1
    output_rows = []
    for out_y in range(input_image.height + 2 * expansion):
        output_row = ''
        for out_x in range(input_image.width + 2 * expansion):
            alg_index = input_image.get_square_value(out_x - expansion, out_y - expansion, void_is_lit)
            output_row += algorithm[alg_index]
        output_rows.append(output_row)
    return Image(output_rows)

(algorithm, input_image) = parse_input()

print(f'{input_image.width} x {input_image.height}')
input_image.print()
print()
output_image = input_image
for i in range(2):
    output_image = enhance(output_image, algorithm, i)
    output_image.print()
    print()

num_lit = 0
for y in range(output_image.height):
    for x in range(output_image.width):
        if output_image.is_lit(x, y, False):
            num_lit += 1
print(num_lit)
