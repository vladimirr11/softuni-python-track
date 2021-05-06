username = input()


while True:
    command = input().split()
    if ' '.join(command) == 'Sign up':
        break

    if ' '.join(command) == 'Case lower':
        username = username.lower()
        print(f'{username}')
    
    if ' '.join(command) == 'Case upper':
        username = username.upper()
        print(f'{username}')
    
    if command[0] == 'Reverse':
        start_index, end_index = command[1], command[2]
        if int(start_index) < int(end_index) < len(username):
            s = ''
            for char in reversed(username[int(start_index):int(end_index) + 1]):
                s += char
            print(s)
    
    if command[0] == 'Cut':
        substring = command[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    
    if command[0] == 'Replace':
        char = command[1]
        username = username.replace(char, '*')
        print(username)
    
    if command[0] == 'Check':
        char = command[1]
        if char in username:
            print(f'Valid')
        else:
            print(f'Your username must contain {char}.')