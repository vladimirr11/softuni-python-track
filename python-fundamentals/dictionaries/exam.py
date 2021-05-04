my_dict = {}

while True:
    command = input().split(':')
    if command[0] == 'Results':
        break

    if command[0] == 'Add':
        person_name = command[1]
        health = int(command[2])
        energy = int(command[3])

        if person_name not in my_dict:
            my_dict[person_name] = [health, energy]
        else:
            my_dict[person_name][0] += health
            # my_dict[person_name][1] += energy
        
    if command[0] == 'Attack':
        attacker = command[1]
        defender = command[2]
        damage = int(command[3])

        if attacker in my_dict and defender in my_dict:
            my_dict[defender][0] -= damage
            if my_dict[defender][0] <= 0:
                print(f'{defender} was disqualified!')
                del my_dict[defender]

            my_dict[attacker][1] -= 1
            if my_dict[attacker][1] <= 0:
                print(f'{attacker} was disqualified!')
                del my_dict[attacker]
    
    if command[0] == 'Delete':
        username = command[1]

        if username in my_dict and username != 'All':
            del my_dict[username]

        if username == 'All':
            my_dict.clear()


sorted_dict = dict(sorted(my_dict.items(), key = lambda x: (-x[1][0], x[0])))

print(f'People count: {len(sorted_dict)}')
for k, v in sorted_dict.items():
    print(f'{k} - {v[0]} - {v[1]}')