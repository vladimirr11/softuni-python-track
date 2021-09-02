def read_square_matrix(side):
    """
    """
    matrix = []
    for _ in range(side):
        values = [int(x) for x in input().split()]
        matrix.append(values)
    
    return matrix


def calculate_diagonal_differences(matrix):
    """
    """
    primary_diagonal = []
    for i in range(len(matrix)):
        primary_diagonal.append(matrix[i][i])
    
    secondary_diagonal = []
    for i in range(len(matrix)):
        secondary_diagonal.append(matrix[i][len(matrix) - i - 1])
    
    absolute_differences = abs(sum(primary_diagonal) - sum(secondary_diagonal))    

    print(absolute_differences)

    
calculate_diagonal_differences(read_square_matrix(int(input())))
