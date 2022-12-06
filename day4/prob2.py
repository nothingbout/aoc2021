with open('input.txt', 'r') as f:
    input_lines = [line.rstrip('\r\n') for line in f.readlines()]

random_nums = [int(x) for x in input_lines[0].split(',')]

board_w = 5
board_h = 5
boards_nums = []

for line_index in range(2, len(input_lines), 6):
    board_lines = input_lines[line_index:line_index + board_h]
    nums = []
    for board_line in board_lines:
        nums.append([int(x) for x in board_line.split()])
    boards_nums.append(nums)

boards_marks = []
for _ in boards_nums:
    marks = []
    for _ in range(board_h):
        marks.append([0] * board_w)
    boards_marks.append(marks)

def mark_board(board_nums, board_marks, num):
    for y in range(board_h):
        for x in range(board_w):
            if boards_nums[b][y][x] == num:
                boards_marks[b][y][x] = 1
                return (x, y)

def check_win(board_marks, check_coords):
    win = True
    for x in range(board_w):
        if board_marks[check_coords[1]][x] != 1:
            win = False
            break
    if win: return True

    win = True
    for y in range(board_h):
        if board_marks[y][check_coords[0]] != 1:
            win = False
            break
    if win: return True
    return False

def unmarked_sum(board_nums, board_marks):
    sum = 0
    for y in range(board_h):
        for x in range(board_w):
            if board_marks[y][x] != 1:
                sum += board_nums[y][x]
    return sum

stop = False
winners_count = 0
already_won = [False] * len(boards_nums)
for num in random_nums:
    for b in range(len(boards_nums)):
        if already_won[b]: continue
        coords = mark_board(boards_nums[b], boards_marks[b], num)
        if coords:
            if check_win(boards_marks[b], coords):
                already_won[b] = True
                winners_count += 1
                if winners_count == len(boards_nums):
                    stop = True
                    print(unmarked_sum(boards_nums[b], boards_marks[b]) * num);
                    break
    if stop: break
