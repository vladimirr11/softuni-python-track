def create_blank_matrix():
    """
    """
    num_rows, num_cols = list(map(int, input().split()))

    blank_matrix = []
    for r in range(num_rows):
        blank_matrix.append([0] * num_cols)
    
    return blank_matrix


def iterate_over_string(string, index):
    """
    """
    if index >= len(string):
        index = index % len(string)

    return string[index]


def fill_blank_matrix(blank_matrix):
    """
    """
    filling_string = input()

    LEN_ROWS = len(blank_matrix)
    LEN_COLS = len(blank_matrix[0])

    counter_idx = 0
    for row in range(LEN_ROWS):
        if row % 2 == 0:
            for col in range(LEN_COLS):
                blank_matrix[row][col] = iterate_over_string(filling_string, counter_idx)
                counter_idx += 1
        else:
            for col in range(LEN_COLS):
                blank_matrix[row][LEN_COLS - col - 1] = iterate_over_string(filling_string, counter_idx)
                counter_idx += 1

    for row in blank_matrix:
        print(''.join(row))


fill_blank_matrix(create_blank_matrix())
