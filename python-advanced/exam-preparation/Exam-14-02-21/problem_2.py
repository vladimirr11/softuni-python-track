def read_matrix(field_size):
    matrix = []
    for _ in range(field_size):
        values = [x for x in input().split()]
        matrix.append(values)

    return matrix


field_size = int(input())
matrix = read_matrix(field_size)


def make_move(matrix, start_row, start_col, command):
    """
    """
    if command == 'right':
        if start_col + 1 >= len(matrix):
            return 'out of field'
        elif matrix[start_row][start_col + 1] == 'X':
            return 'wall'
        else:
            value = matrix[start_row][start_col + 1]
            return (start_row, start_col + 1, value)
    
    if command == 'left':
        if start_col - 1 < 0:
            return 'out of field'
        elif matrix[start_row][start_col - 1] == 'X':
            return 'wall'
        else:
            value = matrix[start_row][start_col - 1]
            return (start_row, start_col - 1, value)
    
    if command == 'up':
        if start_row - 1 < 0:
            return 'out of field'
        elif matrix[start_row - 1][start_col] == 'X':
            return 'wall'
        else:
            value = matrix[start_row - 1][start_col]
            return (start_row - 1, start_col, value)

    if command == 'down':
        if start_row + 1 >= len(matrix):
            return 'out of field'
        elif matrix[start_row + 1][start_col] == 'X':
            return 'wall'
        else:
            value = matrix[start_row + 1][start_col]
            return (start_row + 1, start_col, value)


colleted_coins = 0

possible_commands = ['right', 'left', 'up', 'down']
hit_wall = False
out_of_filed = False

moves_list = []


for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'P':

            while colleted_coins <= 100:
                command = input()
                if command not in possible_commands:
                    continue

                result_move = make_move(matrix, row, col, command)
                if result_move == 'wall':
                    hit_wall = True
                    colleted_coins = colleted_coins // 2
                    break
                elif result_move == 'out of field':
                    out_of_filed = True
                    colleted_coins = colleted_coins // 2
                    break
                else:
                    row, col, value = result_move
                    colleted_coins += int(value)
                    moves_list.append((row, col))


if hit_wall or out_of_filed:
    print(f"Game over! You've collected {colleted_coins} coins.")
    print(f"Your path:")
else:
    print(f"You won! You've collected {colleted_coins} coins.")
    print(f"Your path:")


for move in moves_list:
    print(f"[{move[0]}, {move[1]}]")
