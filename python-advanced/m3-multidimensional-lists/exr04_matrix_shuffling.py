rows, _ = list(map(int, input().split()))


def read_matrix(rows: int):
    matrix = []
    for _ in range(rows):
        matrix_entries = [x for x in input().split()]
        matrix.append(matrix_entries)

    return matrix


def validate_matrix_indices(matrix: list, args: tuple):
    row_one, col_one, row_two, col_two = args

    NUM_ROWS = len(matrix)
    NUM_COLS = len(matrix[0])

    if row_one > NUM_ROWS or row_two > NUM_ROWS or col_one > NUM_COLS or col_two > NUM_COLS:
        return 'Invalid input!'

    return


def shuffle_matrix(matrix: list, args: tuple):
    row_one, col_one, row_two, col_two = args

    (matrix[row_one][col_one], matrix[row_two][col_two]) = (
        matrix[row_two][col_two], matrix[row_one][col_one])

    return matrix


matrix = read_matrix(rows)
LEN_VALID_COMMAND = 5
while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] == 'swap' and len(command) == LEN_VALID_COMMAND:
        swapping_indices = tuple(int(command[i])
                                 for i in range(1, LEN_VALID_COMMAND))
        if validate_matrix_indices(matrix, swapping_indices) is not None:
            print(validate_matrix_indices(matrix, swapping_indices))
            continue

        shuffled_matrix = shuffle_matrix(matrix, swapping_indices)
        for r in range(len(shuffled_matrix)):
            [print(shuffled_matrix[r][c], end=' ')
             for c in range(len(shuffled_matrix[0]))]
            print()
    else:
        print('Invalid input!')
