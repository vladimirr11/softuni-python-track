rows = int(input())
directions = input().split()


def read_miner_field(rows):
    miner_field = []
    for _ in range(rows):
        field_entries = [x for x in input().split()]
        miner_field.append(field_entries)
    
    return miner_field


def find_start_position(miner_field):
    start_row, start_col = 0, 0
    for row_idx in range(len(miner_field)):
        for col_idx in range(len(miner_field[row_idx])):
            if miner_field[row_idx][col_idx] == 's':
                start_row, start_col = row_idx, col_idx
    
    return (start_row, start_col)


def count_coals(miner_field):
    counter_coals = 0
    for r in range(len(miner_field)):
        for c in range(len(miner_field[0])):
            if miner_field[r][c] == 'c':
                counter_coals += 1
    
    return counter_coals


miner_field = read_miner_field(rows)

start_row_idx, start_col_idx = find_start_position(miner_field)

number_coals = count_coals(miner_field)

is_coal_collected = False
is_game_finished = False


curr_row_poss, curr_col_poss = start_row_idx, start_col_idx
for dir in directions:
    if number_coals == 0:
        is_coal_collected = True
        break

    if dir == 'up':
        if curr_row_poss - 1 < 0:
            continue
        curr_row_poss -= 1
        if miner_field[curr_row_poss][curr_col_poss] == 'c':
            number_coals -= 1
            miner_field[curr_row_poss][curr_col_poss] = '*'
        elif miner_field[curr_row_poss][curr_col_poss] == 'e':
            is_game_finished = True
            break
    elif dir == 'down':
        if curr_row_poss + 1 == len(miner_field):
            continue
        curr_row_poss += 1
        if miner_field[curr_row_poss][curr_col_poss] == 'c':
            number_coals -= 1
            miner_field[curr_row_poss][curr_col_poss] = '*'
        elif miner_field[curr_row_poss][curr_col_poss] == 'e':
            is_game_finished = True
            break
    elif dir == 'left':
        if curr_col_poss - 1 < 0:
            continue
        curr_col_poss -= 1
        if miner_field[curr_row_poss][curr_col_poss] == 'c':
            number_coals -= 1
            miner_field[curr_row_poss][curr_col_poss] = '*'
        elif miner_field[curr_row_poss][curr_col_poss] == 'e':
            is_game_finished = True
            break
    elif dir == 'right':
        if curr_col_poss + 1 == len(miner_field[0]):
            continue
        curr_col_poss += 1
        if miner_field[curr_row_poss][curr_col_poss] == 'c':
            number_coals -= 1
            miner_field[curr_row_poss][curr_col_poss] = '*'
        elif miner_field[curr_row_poss][curr_col_poss] == 'e':
            is_game_finished = True
            break


if is_coal_collected:
    print(f'You collected all coals! ({curr_row_poss}, {curr_col_poss})')
elif is_game_finished:
    print(f'Game over! ({curr_row_poss}, {curr_col_poss})')
elif number_coals == 0:
    print(f'You collected all coals! ({curr_row_poss}, {curr_col_poss})')
else:
    print(f'{number_coals} coals left. ({curr_row_poss}, {curr_col_poss})')
