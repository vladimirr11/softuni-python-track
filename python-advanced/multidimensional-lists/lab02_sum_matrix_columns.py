def get_matrix_columns_sum():
    """
    """
    num_rows, num_cols = list(map(int, input().split(', ')))

    matrix = []
    for col in range(num_rows):
        values = [int(x) for x in input().split()]
        matrix.append(values)

    cols_sum = [0] * num_cols
    for row in range(num_rows):
        for col in range(num_cols):
            cols_sum[col] += matrix[row][col]
    
    return cols_sum


columns_sum = get_matrix_columns_sum()

for col_sum in columns_sum:
    print(col_sum)
    