rows, _ = list(map(int, input().split(', ')))


def sum_matrix_elements(rows):
    sum_matrix = 0
    matrix = []
    for _ in range(rows):
        values = [int(x) for x in input().split(', ')]
        for val in values:
            sum_matrix += val
        matrix.append(values)
        
    print(sum_matrix)
    print(matrix)


sum_matrix_elements(rows)
