def get_sides_of_matrix():
    num_rows, num_cols = list(map(int, input().split(', ')))
    return (num_rows, num_cols)


def make_matrix(sides):
    num_rows, _ = sides

    matrix = []
    for _ in range(num_rows):
        values = [int(x) for x in input().split(', ')]
        matrix.append(values)
    
    return matrix


def get_submatrix_sum(matrix, row, col):
    return matrix[row][col] + matrix[row][col + 1] + \
            matrix[row + 1][col] + matrix[row + 1][col + 1]


def print_submatrix(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=' ')
        print()


def find_biggest_top_left_matrix(matrix):
    max_value_index = (0, 0)
    max_value_sum = get_submatrix_sum(matrix, 0, 0)

    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            current_max_value_sum = get_submatrix_sum(matrix, row, col)
            if max_value_sum < current_max_value_sum:
                max_value_sum = current_max_value_sum
                max_value_index = (row, col)
    
    max_row_index, max_col_index = max_value_index
    print_submatrix(matrix, max_row_index, max_col_index)
    
    print(max_value_sum)


find_biggest_top_left_matrix(make_matrix(get_sides_of_matrix()))
