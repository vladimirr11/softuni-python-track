my_dict = {}

while True:
    string_input = input()
    if string_input == 'end':
        break

#   reversed_string = ''.join(reversed(string_input))
    reversed_string = string_input[::-1]

    if string_input not in my_dict:
        my_dict[string_input] = ''

    my_dict[string_input] = reversed_string

for k, v in my_dict.items():
    print(f'{k} = {v}')
