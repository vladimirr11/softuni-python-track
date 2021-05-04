number_of_commands = int(input())

registered_dict = {}

for _ in range(number_of_commands):
    string_input = input().split()
    command = string_input[0]
    user_name = string_input[1]

    if command == 'register':
        ticket_number = string_input[2]

        if user_name in registered_dict:
            print(f'ERROR: already registered with plate number {registered_dict[user_name]}')
            continue

        registered_dict[user_name] = ticket_number
        print(f'{user_name} registered {ticket_number} successfully')

    elif command == 'unregister':
        if user_name not in registered_dict:
            print(f'ERROR: user{user_name} not found')
            continue

        registered_dict.pop(user_name)
        print(f'{user_name} unregistered successfully')

for k, v in registered_dict.items():
    print(f'{k} => {v}')