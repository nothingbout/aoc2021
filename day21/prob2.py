input_file = 'input.txt'

def parse_input():
    with open(input_file, 'r') as f:
        lines = [line.rstrip('\r\n') for line in f.readlines()]

    return [int(lines[0].split()[4]) - 1, int(lines[1].split()[4]) - 1]

def increment_state_count(state_counts, state, amount):
    state_counts[state] = state_counts.get(state, 0) + amount

player_positions = parse_input()
state_counts = {(player_positions[0], player_positions[1], 0, 0): 1}

is_player1_turn = True

while True:
    had_unresolved_states = False
    new_state_counts = {}

    for state, count in state_counts.items():
        pos1, pos2, score1, score2 = state

        if score1 >= 21 or score2 >= 21:
            increment_state_count(new_state_counts, state, count)
        else:
            had_unresolved_states = True
            for d1 in range(1, 4):
                for d2 in range(1, 4):
                    for d3 in range(1, 4):
                        total = d1 + d2 + d3
                        if is_player1_turn:
                            new_pos = (pos1 + total) % 10
                            new_state = (new_pos, pos2, score1 + new_pos + 1, score2)
                        else:
                            new_pos = (pos2 + total) % 10
                            new_state = (pos1, new_pos, score1, score2 + new_pos + 1)
                        increment_state_count(new_state_counts, new_state, count)

    state_counts = new_state_counts
    is_player1_turn = not is_player1_turn
    if not had_unresolved_states: break;

player1_wins = 0
player2_wins = 0

for state, count in state_counts.items():
    _, _, score1, score2 = state
    if score1 >= 21: player1_wins += count
    elif score2 >= 21: player2_wins += count
    else: raise "wut"

print(f'{player1_wins} {player2_wins}')
print(max(player1_wins, player2_wins))
