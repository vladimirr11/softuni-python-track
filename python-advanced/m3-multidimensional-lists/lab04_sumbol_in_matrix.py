def find_symbol(matrix, symbol):
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == symbol:
                return (row, col)

    return None


n = int(input())
matrix = [input() for _ in range(n)]
symbol = input()

result = find_symbol(matrix, symbol)

if result:
    (row, col) = result
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')
    