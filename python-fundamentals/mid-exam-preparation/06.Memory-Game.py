sequence = input().split()

moves = 0
is_won = 0
handle_two = False
handle = True

while True:
    command = input().split()

    if handle:
        moves += 1

    if command[0] == 'end':
        break

    index_one = int(command[0])
    index_two = int(command[1])

    if len(sequence) > 0 and sequence[index_one] == sequence[index_two]:
        elem_to_remove = sequence[index_two]
        sequence.remove(elem_to_remove)
        sequence.remove(elem_to_remove)
        print(f'Congrats! You have found matching elements - {elem_to_remove}!')
    else:
        if index_one == index_two or index_one < 0 or index_two < 0 or index_one > len(sequence) or index_two > len(sequence):
            if len(sequence) > 0:
                mid_index = len(sequence) // 2
                value_to_insert = '-' + str(moves) + 'a'
                sequence.insert(mid_index, value_to_insert)
                sequence.insert(mid_index, value_to_insert)
                print('Invalid input! Adding additional elements to the board')
        else:
            if sequence[index_one] != sequence[index_two]:
                if len(sequence) > 0:
                    print('Try again!')

    if len(sequence) == 0:
        is_won = moves 
        handle = False
        handle_two = True
        exit()

if handle_two:
    print(f'You have won in {is_won} turns!')
else:
    print('Sorry you lose :(')
    print(' '.join(sequence))