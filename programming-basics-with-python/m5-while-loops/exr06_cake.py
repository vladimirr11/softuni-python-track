width_cake = int(input())
length_cake = int(input())

cake_size = width_cake * length_cake
total_pieces = 0
condition = False

while cake_size > total_pieces:
    pieces_took = input()
    if pieces_took == 'STOP':
        condition = True
        break

    current_pieces = int(pieces_took)
    total_pieces += current_pieces


if condition:
    print(f'{cake_size - total_pieces} pieces are left.')
else:
    print(
        f'No more cake left! You need {abs(cake_size - total_pieces)} pieces more.')
