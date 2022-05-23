def read_matrix():
    matrix = []
    for _ in range(8):
        values = [x for x in input().split()]
        matrix.append(values)

    return matrix


matrix = read_matrix()

queens_list = []


def right_move(matrix, start_row_idx, start_col_idx):
    for col in range(start_col_idx, len(matrix) - 1):
        if matrix[start_row_idx][col + 1] == 'Q':
            return
        elif matrix[start_row_idx][col + 1] == 'K':
            return True


def left_move(matrix, start_row_idx, start_col_idx):
    for col in range(start_col_idx, 1, -1):
        if matrix[start_row_idx][col - 1] == 'Q':
            return
        elif matrix[start_row_idx][col - 1] == 'K':
            return True


def up_move(matrix, start_row_idx, start_col_idx):
    for row in range(start_row_idx, 1, -1):
        if matrix[row - 1][start_col_idx] == 'Q':
            return
        elif matrix[row - 1][start_col_idx] == 'K':
            return True


def down_move(matrix, start_row_idx, start_col_idx):
    for row in range(start_row_idx, len(matrix) - 1):
        if matrix[row + 1][start_col_idx] == 'Q':
            return
        elif matrix[row + 1][start_col_idx] == 'K':
            return True


def left_up_diagonal(matrix, start_row_idx, start_col_idx):
    counter = 0
    for row in range(start_row_idx, 1, -1):
        counter += 1
        if start_col_idx - counter == 0:
            return

        if matrix[row - 1][start_col_idx - counter] == 'Q':
            return
        elif matrix[row - 1][start_col_idx - counter] == 'K':
            return True


def left_down_diagonal(matrix, start_row_idx, start_col_idx):
    counter = 0
    for row in range(start_row_idx, len(matrix) - 1):
        counter += 1
        if start_col_idx - counter == 0:
            return

        if matrix[row + 1][start_col_idx - counter] == 'Q':
            return
        elif matrix[row + 1][start_col_idx - counter] == 'K':
            return True


def right_up_diagonal(matrix, start_row_idx, start_col_idx):
    counter = 0
    for row in range(start_row_idx, 1, -1):
        counter += 1
        if counter + start_col_idx == len(matrix):
            return

        if matrix[row - 1][start_col_idx + counter] == 'Q':
            return
        elif matrix[row - 1][start_col_idx + counter] == 'K':
            return True


def right_down_diagonal(matrix, start_row_idx, start_col_idx):
    counter = 0
    for row in range(start_row_idx, len(matrix) - 1):
        counter += 1
        if counter + start_col_idx == len(matrix):
            return

        if matrix[row + 1][start_col_idx + counter] == 'Q':
            return
        elif matrix[row + 1][start_col_idx + counter] == 'K':
            return True


for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'Q':
            if right_move(matrix, row, col):
                queens_list.append((row, col))
            if left_move(matrix, row, col):
                queens_list.append((row, col))
            if up_move(matrix, row, col):
                queens_list.append((row, col))
            if down_move(matrix, row, col):
                queens_list.append((row, col))
            if left_up_diagonal(matrix, row, col):
                queens_list.append((row, col))
            if left_down_diagonal(matrix, row, col):
                queens_list.append((row, col))
            if right_up_diagonal(matrix, row, col):
                queens_list.append((row, col))
            if right_down_diagonal(matrix, row, col):
                queens_list.append((row, col))


if not queens_list:
    print('The king is safe!')
else:
    for indices in queens_list:
        print(f'[{indices[0]}, {indices[1]}]')
