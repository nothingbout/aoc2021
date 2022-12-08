import heapq

input_file = 'input.txt'

class Dungeon:
    def __init__(self, rooms, hallways = None):
        self.rooms = rooms
        self.hallways = hallways if hallways else [() for _ in range(2 * len(rooms) + 3)]
        self.rooms_count = len(self.rooms)
        self.hallways_count = len(self.hallways)

    def copy(self):
        return Dungeon(self.rooms.copy(), self.hallways.copy())
            
    def __hash__(self):
        return hash(tuple(self.rooms) + tuple(self.hallways))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.rooms == other.rooms and self.hallways == other.hallways

    def print(self):
        for i in range(2):
            ss = ''
            for j in range(len(self.hallways)):
                hallway = self.hallways[j]
                ss += (str(hallway[i]) if i < len(hallway) else ('.' if i < self.hallway_size(j) else ' '))
            print(ss)

        for i in range(1, -1, -1):
            ss = '  '
            for room in self.rooms:
                ss += (str(room[i]) if i < len(room) else '.') + ' '
            print(ss)
        print('')

    def hallway_size(self, i):
        return 1

    def is_room_empty(self, i):
        return len(self.rooms[i]) == 0

    def is_hallway_empty(self, i):
        return len(self.hallways[i]) == 0

    def is_room_full(self, i):
        return len(self.rooms[i]) >= 2

    def is_hallway_full(self, i):
        return len(self.hallways[i]) >= self.hallway_size(i)

    def is_hallway_next_to_room(self, i):
        for j in range(4):
            if i == self.first_hallway_from_room(j): return True
        return False

    def first_hallway_from_room(self, i):
        return 2 + 2 * i

    def is_room_occupied_by_other_types(self, room_index, type):
        for occupier in self.rooms[room_index]:
            if occupier != type: return True
        return False

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    rooms = [[] for _ in range(4)]
    for line in lines[2:4]:
        for i in range(4):
            rooms[i].insert(0, ord(line[3 + 2 * i]) - ord('A'))

    rooms = [tuple(room) for room in rooms]
    return rooms

def room_to_hallway_possible(dungeon, from_room, to_hallway):
    if dungeon.is_hallway_next_to_room(to_hallway): return False
    if dungeon.is_room_empty(from_room): return False
    room_hallway = dungeon.first_hallway_from_room(from_room)
    if to_hallway <= room_hallway:
        for i in range(to_hallway, room_hallway + 1):
            if dungeon.is_hallway_full(i): return False
    else:
        for i in range(room_hallway, to_hallway + 1):
            if dungeon.is_hallway_full(i): return False
    return True

def hallway_to_room_possible(dungeon, from_hallway, to_room):
    if dungeon.is_hallway_empty(from_hallway): return False
    mover_type = dungeon.hallways[from_hallway][-1]
    if mover_type != to_room: return False
    if dungeon.is_room_full(to_room): return False
    if dungeon.is_room_occupied_by_other_types(to_room, mover_type): return False

    room_hallway = dungeon.first_hallway_from_room(to_room)
    if from_hallway <= room_hallway:
        for i in range(from_hallway + 1, room_hallway + 1):
            if dungeon.is_hallway_full(i): return False
    else:
        for i in range(room_hallway, from_hallway):
            if dungeon.is_hallway_full(i): return False
    return True

def get_all_possible_moves(dungeon):
    all_moves = []
    for from_room in range(dungeon.rooms_count):
        for to_hallway in range(dungeon.hallways_count):
            if room_to_hallway_possible(dungeon, from_room, to_hallway):
                all_moves.append((True, from_room, to_hallway))

    for from_hallway in range(dungeon.hallways_count):
        for to_room in range(dungeon.rooms_count):
            if hallway_to_room_possible(dungeon, from_hallway, to_room):
                all_moves.append((False, from_hallway, to_room))
    return all_moves

type_move_costs = [1, 10, 100, 1000]
def get_move_cost(dungeon, move):
    (is_from_room, from_index, to_index) = move
    if is_from_room:
        room_hallway = dungeon.first_hallway_from_room(from_index)
        mover_type = dungeon.rooms[from_index][-1]
        steps = room_hallway - to_index + 1 if to_index <= room_hallway else to_index - room_hallway + 1
        if len(dungeon.rooms[from_index]) == 1: steps += 1
    else:
        room_hallway = dungeon.first_hallway_from_room(to_index)
        mover_type = dungeon.hallways[from_index][-1]
        steps = room_hallway - from_index + 1 if from_index <= room_hallway else from_index - room_hallway + 1
        if len(dungeon.rooms[to_index]) == 0: steps += 1
    return type_move_costs[mover_type] * steps

def make_move(dungeon, move):
    dungeon = dungeon.copy()
    (is_from_room, from_index, to_index) = move
    if is_from_room:
        room = dungeon.rooms[from_index]
        movers = room[-1:]
        dungeon.rooms[from_index] = room[:-1]
        dungeon.hallways[to_index] += movers
    else:
        hallway = dungeon.hallways[from_index]
        movers = hallway[-1:]
        dungeon.hallways[from_index] = hallway[:-1]
        dungeon.rooms[to_index] += movers
    return dungeon

def is_solved(dungeon):
    for i in range(len(dungeon.rooms)):
        room = dungeon.rooms[i]
        if len(room) != 2 or room[0] != i: return False
    return True

rooms = parse_input()
# print(rooms)

start_dungeon = Dungeon(rooms)
start_dungeon.print()

dungeon_min_costs = {start_dungeon: 0}
dungeon_min_moves = {}
search_from_dungeons = [(0, id(start_dungeon), start_dungeon)]
heapq.heapify(search_from_dungeons)
# heapq.heappush(search_from_dungeons, (1, start_dungeon));  
# heapq.heappush(search_from_dungeons, (2, start_dungeon));  

while len(search_from_dungeons) > 0:
    (from_cost, _, from_dungeon) = heapq.heappop(search_from_dungeons)

    all_moves = get_all_possible_moves(from_dungeon)
    for move in all_moves:
        move_cost = get_move_cost(from_dungeon, move)
        to_dungeon = make_move(from_dungeon, move)

        to_cost = dungeon_min_costs.get(to_dungeon, -1)
        if to_cost < 0 or from_cost + move_cost < to_cost:
            new_to_cost = from_cost + move_cost
            dungeon_min_costs[to_dungeon] = new_to_cost

            dungeon_min_moves[to_dungeon] = (from_dungeon, move)

            if not is_solved(to_dungeon):
                heapq.heappush(search_from_dungeons, (new_to_cost, id(to_dungeon), to_dungeon));  

min_cost = -1
min_cost_dungeon = None
for dungeon in dungeon_min_costs.keys():
    if is_solved(dungeon):
        cost = dungeon_min_costs[dungeon]
        if min_cost < 0 or cost < min_cost: 
            min_cost = cost
            min_cost_dungeon = dungeon

min_cost_dungeon.print()

dungeon = min_cost_dungeon
while True:
    from_state = dungeon_min_moves.get(dungeon, None)
    if not from_state: break
    (from_dungeon, move) = from_state

    print(f'{move}: {get_move_cost(from_dungeon, move)}')
    print('')

    from_dungeon.print()

    dungeon = from_dungeon

print(min_cost)

# test_dungeon = start_dungeon.copy()
# test_dungeon = make_move(test_dungeon, (True, 0, 2))
# test_dungeon = make_move(test_dungeon, (True, 0, 0))
# test_dungeon = make_move(test_dungeon, (True, 3, 4))
# test_dungeon = make_move(test_dungeon, (True, 3, 4))
# test_dungeon.print()

# all_moves = get_all_possible_moves(test_dungeon)
# print(all_moves)
# print([get_move_cost(test_dungeon, move) for move in all_moves])

# start_dungeon.print()
