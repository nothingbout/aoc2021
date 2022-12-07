class ProbeState:
    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def __str__(self):
        return f'({self.pos_x},{self.pos_y})/({self.vel_x},{self.vel_y})'

    def copy(self):
        return ProbeState(self.pos_x, self.pos_y, self.vel_x, self.vel_y)

    def simulate(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        if self.vel_x > 0: self.vel_x -= 1
        elif self.vel_x < 0: self.vel_x += 1
        self.vel_y -= 1

class Area:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def __str__(self):
        return f'({self.min_x},{self.max_x})/({self.min_y},{self.max_y})'

    def contains(self, x, y):
        return x >= self.min_x and x <= self.max_x and y >= self.min_y and y <= self.max_y

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\r\n') for line in f.readlines()]

for line in lines:
    parts = line.split()
    x_parts = parts[2].split('..')
    y_parts = parts[3].split('..')

    area = Area(int(x_parts[0][2:]), int(x_parts[1][:-1]), int(y_parts[0][2:]), int(y_parts[1]))
    print(area)

win_max_y = 0

for start_vel_y in range(0, 500):

    for start_vel_x in range(0, 100):
        win = False

        state = ProbeState(0, 0, start_vel_x, start_vel_y)
        max_y = 0
        while state.pos_y >= area.min_y:
            state.simulate()
            max_y = max(max_y, state.pos_y)
            if area.contains(state.pos_x, state.pos_y):
                win = True
                print(f'win: {start_vel_x}, {start_vel_y}, max y: {max_y}')
                break

        if win: 
            win_max_y = max(win_max_y, max_y)
            break

print(f'best win: {win_max_y}')