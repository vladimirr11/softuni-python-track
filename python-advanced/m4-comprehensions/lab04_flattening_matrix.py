def flatten_matrix(num_rows):
    matrix = [list(map(int, input().split(', '))) for _ in range(num_rows)]
    flattened_matrix = [num for row in matrix for num in row]

    return flattened_matrix


print(flatten_matrix(int(input())))
