def create_square_matrix(N):
    """
    """
    matrix = []
    for _ in range(N):
        values = list(map(int, input().split()))
        matrix.append(values)
    
    return matrix


def get_bombs_coordinates():
    """
    """
    bombs_coordinates =[tuple(map(int, bomb.split(','))) for bomb in input().split()]

    return bombs_coordinates


def kill_cells(matrix, coordinates):
    """
    """
    row_indx, col_indx = coordinates
    core_value = matrix[row_indx][col_indx]
    for r in range(row_indx - 1, row_indx + 2):
        for c in range(col_indx - 1, col_indx + 2):
            if (r >= 0 and r < len(matrix)) and (c >= 0 and c < len(matrix)):
                if matrix[r][c] > 0:
                    matrix[r][c] -= core_value

    return matrix


def detonate_bombs(matrix):
    """
    """
    bombs_coordinates = get_bombs_coordinates()

    LEN_SIDE_MATRIX = len(matrix)

    for bomb in bombs_coordinates:
        for row in range(LEN_SIDE_MATRIX):
            for col in range(LEN_SIDE_MATRIX):
                if bomb[0] == row and bomb[1] == col:
                    kill_cells(matrix, bomb)
    
    return matrix


def print_result(matrix):
    """
    """
    count_live_cells = 0
    sum_live_cells = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] > 0:
                count_live_cells += 1
                sum_live_cells += matrix[r][c]
    
    print(f'Alive cells: {count_live_cells}')
    print(f'Sum: {sum_live_cells}')

    for row in matrix:
        print(' '.join(list(map(str, row))))


print_result(detonate_bombs(create_square_matrix(int(input()))))
