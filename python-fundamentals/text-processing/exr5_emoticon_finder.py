string_input = input()

emoticon = ''

for i in range(len(string_input)):
    if string_input[i] == ':':
        if i + 1 >= len(string_input):
            continue

        if string_input[i + 1] != ' ':
            print(f':{string_input[i + 1]}')