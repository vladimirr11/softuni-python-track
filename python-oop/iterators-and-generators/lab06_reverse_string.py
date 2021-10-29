def reverse_text(string):
    rev_string = string[::-1]
    for idx in range(len(rev_string)):
        yield rev_string[idx]


if __name__ == '__main__':
    for char in reverse_text('step'):
        print(char, end='')
        