input_file = 'input.txt'

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    return [int(lines[0].split()[4]) - 1, int(lines[1].split()[4]) - 1]

dice_next = 1
player_positions = parse_input()
player_scores = [0] * len(player_positions)
turn = 0
rolls = 0
while True:
    pos = player_positions[turn]

    total = 0
    for _ in range(3):
        total += dice_next
        rolls += 1
        dice_next += 1
        if dice_next > 100: dice_next = 1

    new_pos = (pos + total) % 10
    player_scores[turn] += new_pos + 1
    player_positions[turn] = new_pos
    
    print(f'player {turn} score {player_scores[turn]}')

    if player_scores[turn] >= 1000: break
    turn = (turn + 1) % len(player_positions)

loser = (turn + 1) % len(player_positions)
loser_score = player_scores[loser]

print(loser_score * rolls)
