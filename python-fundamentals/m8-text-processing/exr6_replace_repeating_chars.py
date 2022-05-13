string_input = input()

for i in range(len(string_input)):
    char = string_input[i]

    if i + 1 == len(string_input):
        print(char, end='')
        break

    next_char = string_input[i + 1]

    if char != next_char:
        print(char, end='')
