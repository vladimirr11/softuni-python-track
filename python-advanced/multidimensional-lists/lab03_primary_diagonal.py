def make_square_matrix(side):
    """
    """
    matrix = []
    for _ in range(side):
        values = [int(x) for x in input().split()]
        matrix.append(values)

    return matrix


def find_primary_diagonal_sum_of_matrix(matrix):
    """
    """
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])

    return sum(diagonal)


side_matrix = int(input())

print(find_primary_diagonal_sum_of_matrix(make_square_matrix(side_matrix)))



# def sum_primary_diagonal():
#     """
#     """
#     N = int(input())

#     matrix = []
#     for _ in range(N):
#         values = [int(x) for x in input().split()]
#         matrix.append(values)

#     diagonal = []
#     for i in range(N):
#         diagonal.append(matrix[i][i])

#     print(sum(diagonal))


# sum_primary_diagonal()


# def sum_secondary_diagonal():
#     """
#     """
#     N = int(input())

#     matrix = []
#     for _ in range(N):
#         values = [int(x) for x in input().split()]
#         matrix.append(values)
    
#     secondary_diagonal = []
#     for i in range(N):
#         secondary_diagonal.append(matrix[i][N - i -1])

#     print(sum(secondary_diagonal))


# sum_secondary_diagonal()


# def sum_below_primary_diagonal():
#     """
#     """
#     N = int(input())

#     matrix = []
#     for _ in range(N):
#         values = [int(x) for x in input().split()]
#         matrix.append(values)
    
#     below_primary_diagonal = []
#     for row in range(N):
#         for col in range(N):
#             # if row == col:
#             #     break
#             if row < col:
#                 break
#             below_primary_diagonal.append(matrix[row][col])
    
#     print(below_primary_diagonal)


# sum_below_primary_diagonal()


# def sum_below_secondary_diagonal():
#     """
#     """
#     N = int(input())

#     matrix = []
#     for _ in range(N):
#         values = [int(x) for x in input().split()]
#         matrix.append(values)
    
#     below_secondary_diagonal = []
#     for row in range(N):
#         for col in range(N - row -1, N):
#             below_secondary_diagonal.append(matrix[row][col])

#     print(sum(below_secondary_diagonal))


# sum_below_secondary_diagonal()
