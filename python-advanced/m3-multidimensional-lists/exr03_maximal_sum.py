def get_sides_of_matrix():
    num_rows, num_cols = list(map(int, input().split()))
    return (num_rows, num_cols)


def create_matrix(sides):
    num_rows, _ = sides

    matrix = []
    for _ in range(num_rows):
        values = [int(x) for x in input().split()]
        matrix.append(values)
    
    return matrix


def print_max_sum_3x3_submatrix(matrix, start_row_idx, start_col_idx):
    for r in range(start_row_idx, start_row_idx + 3):
        for c in range(start_col_idx, start_col_idx + 3):
            print(matrix[r][c], end=' ')
        print()


def find_max_sum_submatrix(matrix):
    LEN_ROWS = len(matrix)
    LEN_COLS = len(matrix[0])
    
    max_sum = 0
    max_sum_start_indices = (0, 0)
    for row in range(LEN_ROWS - 2):
        for col in range(LEN_COLS - 2):
            sum_submatrix = 0
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    sum_submatrix += matrix[r][c]
            if max_sum < sum_submatrix:
                max_sum = sum_submatrix
                max_sum_start_indices = (row, col)

    print(f'Sum = {max_sum}')
    print_max_sum_3x3_submatrix(matrix, *max_sum_start_indices)      
             

find_max_sum_submatrix(create_matrix(get_sides_of_matrix()))
