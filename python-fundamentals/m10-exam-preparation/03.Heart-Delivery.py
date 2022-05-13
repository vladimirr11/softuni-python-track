neighborhood = list(map(int, input().split('@')))

last_position = 0

while True:
    command = input().split()
    if command[0] == 'Love!':
        break

    if command[0] == 'Jump':
        index = int(command[1])
        current_possition = last_position + index

        if current_possition < len(neighborhood):
            last_position = current_possition
            if neighborhood[current_possition] == 0:
                print(
                    f'Place {current_possition} already had Valentine\'s day.')

            if neighborhood[current_possition] >= 2:
                neighborhood[current_possition] -= 2

                if neighborhood[current_possition] == 0:
                    print(f'Place {current_possition} has Valentine\'s day.')

        if current_possition >= len(neighborhood):
            last_position = 0
            if neighborhood[0] == 0:
                print(f'Place {last_position} already had Valentine\'s day.')

            if neighborhood[0] >= 2:
                neighborhood[0] -= 2
                if neighborhood[0] == 0:
                    print(f'Place {last_position} has Valentine\'s day.')


print(f'Cupid\'s last position was {last_position}.')

counter = 0
for index in range(len(neighborhood)):
    if neighborhood[index] > 0:
        counter += 1

if counter > 0:
    print(f'Cupid has failed {counter} places.')
