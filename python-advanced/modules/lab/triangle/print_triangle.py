def print_triangle(size):
    """
    """
    for i in range(1, size + 1):
        print(i * '*')
    for j in range(size - 1, 0, -1):
        print(j * '*')
        