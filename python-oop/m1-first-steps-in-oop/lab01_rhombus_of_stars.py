def generate_line(idx: int, n: int):
    white_space = ' ' * (n - idx - 1)
    stars = '* ' * (idx + 1)
    return f'{white_space}{stars}'


def print_rhombus_of_stars(n):
    for i in range(n):
        print(generate_line(i, n))

    for j in range(n - 2, -1, -1):
        print(generate_line(j, n))


if __name__ == '__main__':
    print_rhombus_of_stars(int(input()))
