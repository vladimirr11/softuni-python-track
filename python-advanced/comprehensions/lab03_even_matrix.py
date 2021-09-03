def filter_matrix_for_even_numbers(num_rows):
    """
    """
    matrix =[list(map(int, input().split(', '))) for row in range(num_rows)]
    even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]

    return even_matrix


print(filter_matrix_for_even_numbers(int(input())))
