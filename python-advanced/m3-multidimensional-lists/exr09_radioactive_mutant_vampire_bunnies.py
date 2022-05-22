rows, _ = list(map(int, input().split()))


def read_lair(rows):
    lair = []
    for _ in range(rows):
        lair_entries = list(input())
        lair.append(lair_entries)

    return lair


def find_player_possition(lair):
    (row, col) = 0, 0
    for row_idx in range(len(lair)):
        for col_idx in range(len(lair[row_idx])):
            if lair[row_idx][col_idx] == 'P':
                row, col = row_idx, col_idx
    
    return (row, col)


def spread_the_bunnies(lair):
    for r in range(len(lair)):
        for c in range(len(lair[0])):
            if lair[r][c] == 'B':
                if r == 0 and c == 0:
                    lair[r + 1][c] = 'C'
                    lair[r][c + 1] = 'C'
                elif r == len(lair) - 1 and c == 0:
                    lair[r - 1][c] = 'C'
                    lair[r][c + 1] = 'C'
                elif r == 0 and c == len(lair[0]) - 1:
                    lair[r + 1][c] = 'C'
                    lair[r][c - 1] = 'C'
                elif r == len(lair) - 1 and c == len(lair[0]) - 1:
                    lair[r - 1][c] = 'C'
                    lair[r][c - 1] = 'C'
                elif r == 0 and c > 0 and c < len(lair[0]) - 1:
                    lair[r + 1][c] = 'C'
                    lair[r][c + 1] = 'C'
                    lair[r][c - 1] = 'C'
                elif r > 0 and r < len(lair) - 1 and c == 0:
                    lair[r + 1][c] = 'C'
                    lair[r - 1][c] = 'C'
                    lair[r][c + 1] = 'C'
                elif c > 0 and c < len(lair[0]) - 1 and r == len(lair) - 1:
                    lair[r - 1][c] = 'C'
                    lair[r][c - 1] = 'C'
                    lair[r][c + 1] = 'C'
                elif r > 0 and r < len(lair) - 1 and c == len(lair[0]) - 1:
                    lair[r - 1][c] = 'C'
                    lair[r + 1][c] = 'C'
                    lair[r][c - 1] = 'C'
                else:
                    lair[r - 1][c] = 'C'
                    lair[r + 1][c] = 'C'
                    lair[r][c - 1] = 'C'
                    lair[r][c + 1] = 'C'

    return lair


def update_lair(lair):
    for r in range(len(lair)):
        for c in range(len(lair[0])):
            if lair[r][c] == 'C':
                lair[r][c] = 'B'
            elif lair[r][c] == 'P':
                lair[r][c] = '.'

    return lair


lair = read_lair(rows)

directions = list(input())

curr_row_poss, curr_col_poss = find_player_possition(lair)

is_player_died = False


for direction in directions:
    if direction == 'U':
        lair = spread_the_bunnies(lair)
        lair = update_lair(lair)

        curr_row_poss -= 1
        if curr_row_poss < 0:
            curr_row_poss = 0
            break
        elif lair[curr_row_poss][curr_col_poss] == 'B':
            is_player_died = True
            break

    elif direction == 'D':
        lair = spread_the_bunnies(lair)
        lair = update_lair(lair)

        curr_row_poss += 1
        if curr_row_poss == len(lair):
            curr_row_poss -= 1
            break
        elif lair[curr_row_poss][curr_col_poss] == 'B':
            is_player_died = True
            break

    elif direction == 'L':
        lair = spread_the_bunnies(lair)
        lair = update_lair(lair)
    	
        curr_col_poss -= 1
        if curr_col_poss < 0:
            curr_col_poss = 0
            break
        elif lair[curr_row_poss][curr_col_poss] == 'B':
            is_player_died = True
            break

    elif direction == 'R':
        lair = spread_the_bunnies(lair)
        lair = update_lair(lair)

        curr_col_poss += 1
        if curr_col_poss == len(lair[0]):
            curr_col_poss -= 1
            break

        if lair[curr_row_poss][curr_col_poss] == 'B':
            is_player_died = True
            break


for r in range(len(lair)):
    for c in range(len(lair[0])):
        print(lair[r][c], end='')
    print()


if is_player_died:
    print(f'dead: {curr_row_poss} {curr_col_poss}')
else:
    print(f'won: {curr_row_poss} {curr_col_poss}')
