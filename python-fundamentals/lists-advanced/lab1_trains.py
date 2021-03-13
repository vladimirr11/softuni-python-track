num_wagons = int(input())

train = [0 for num_wagon in range(num_wagons)]

while True:
    command = input()
    if command == 'End':
        break
    
    tokens = command.split(' ')
    type_command = tokens[0]

    if type_command == 'add':
        num_people_to_add = int(tokens[1])
        train[-1] += num_people_to_add
    elif type_command == 'insert':
        index = int(tokens[1])
        people_to_insert = int(tokens[2])
        train[index] += people_to_insert
    elif type_command == 'leave':
        wagon_to_remove = int(tokens[1])
        people_to_remove = int(tokens[2])
        train[wagon_to_remove] -= people_to_remove

print(train)
