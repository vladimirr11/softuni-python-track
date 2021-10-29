def read_matrix(field_size):
    matrix = []
    for _ in range(field_size):
        values = [x for x in input().split()]
        matrix.append(values)

    return matrix


wonderland_size = int(input())
matrix = read_matrix(wonderland_size)


def make_move(matrix, start_row, start_col, command):
    """
    """
    if command == 'right':
        if start_col + 1 >= len(matrix):
            return 'out of field'
        elif matrix[start_row][start_col + 1] == 'R':
            return 'rabbit'
        else:
            value = matrix[start_row][start_col + 1]
            return (start_row, start_col + 1, value)
    
    if command == 'left':
        if start_col - 1 < 0:
            return 'out of field'
        elif matrix[start_row][start_col - 1] == 'R':
            return 'rabbit'
        else:
            value = matrix[start_row][start_col - 1]
            return (start_row, start_col - 1, value)
    
    if command == 'up':
        if start_row - 1 < 0:
            return 'out of field'
        elif matrix[start_row - 1][start_col] == 'R':
            return 'rabbit'
        else:
            value = matrix[start_row - 1][start_col]
            return (start_row - 1, start_col, value)

    if command == 'down':
        if start_row + 1 >= len(matrix):
            return 'out of field'
        elif matrix[start_row + 1][start_col] == 'R':
            return 'rabbit'
        else:
            value = matrix[start_row + 1][start_col]
            return (start_row + 1, start_col, value)


collected_tea_bags = 0
moves_list = []

alice_succeeded = True
rabbit_encountered = False

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'A':

            while collected_tea_bags < 10:
                command = input()

                result_move = make_move(matrix, row, col, command)
                if result_move == 'rabbit':
                    rabbit_encountered = True
                    alice_succeeded = False
                    break
                elif result_move == 'out of field':
                    alice_succeeded = False
                    break
                else:
                    row, col, value = result_move
                    if value != '.':
                        collected_tea_bags += int(value)
                    moves_list.append((row, col))


for row in range(len(matrix)):
    for col in range(len(matrix)):
        if (row, col) in moves_list or matrix[row][col] == 'A' or matrix[row][col] == 'R':
            if matrix[row][col] == 'R' and rabbit_encountered == True:
                matrix[row][col] = '*'
            elif matrix[row][col] == 'R' and rabbit_encountered == False:
                matrix[row][col] = 'R'
            else:
                matrix[row][col] = '*'


if alice_succeeded:
    print('She did it! She went to the party.')
else:
    print('Alice didn\'t make it to the tea party.')

for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col], end=' ')
    print()
