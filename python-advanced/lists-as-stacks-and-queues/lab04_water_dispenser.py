from collections import deque


initial_quantity = int(input())
people_queue = deque()


while True:
    command = input()
    if command == 'Start':
        break

    people_queue.append(command)


while True:
    command = input().split()

    if command[0] == 'End':
        print(f'{initial_quantity} liters left')
        break

    elif command[0] == 'refill':
        initial_quantity += int(command[1])

    else:
        if initial_quantity >= int(command[0]):
            initial_quantity -= int(command[0])
            print(f'{people_queue.popleft()} got water')
        else:
            print(f'{people_queue.popleft()} must wait')
