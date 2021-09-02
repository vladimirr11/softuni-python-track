rows, columns = list(map(int, input().split()))

def read_matrix(rows: int):
    """
    """
    matrix = []
    for _ in range(rows):
        entry_chars = [x for x in input().split()]
        matrix.append(entry_chars)
    
    return matrix


def look_for_2x2_squares_of_equal_chars_in_matrix(matrix, rows, cols):
    """
    """
    counter_submatrix = 0
    for row in range(rows - 1):
        for col in range(cols - 1):
            if (matrix[row][col] == matrix[row][col + 1] and \
                matrix[row][col] == matrix[row + 1][col] and \
                matrix[row][col] == matrix[row + 1][col + 1]):
                counter_submatrix += 1
    
    return counter_submatrix


print(look_for_2x2_squares_of_equal_chars_in_matrix(read_matrix(rows), rows, columns))
