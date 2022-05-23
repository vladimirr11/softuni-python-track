def find_square_matrix_diagonals_sums(square_side):
    matrix_values = [[int(v) for v in input().split(', ')] for _ in range(square_side)]

    prime_diagonal_values = [matrix_values[i][i] for i in range(len(matrix_values))]
    secondary_diagonal_values = [matrix_values[i][len(matrix_values) - i - 1] for i in range(len(matrix_values))]
    
    print(f'First diagonal: {", ".join(list(map(str, prime_diagonal_values)))}. Sum: {sum(prime_diagonal_values)}')
    print(f'Second diagonal: {", ".join(list(map(str, secondary_diagonal_values)))}. Sum: {sum(secondary_diagonal_values)}')


find_square_matrix_diagonals_sums(int(input()))
