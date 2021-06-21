from collections import deque


def get_queue_lenght():
    """
    """
    people = deque()

    while True:
        command = input()
        if command == 'End':
            print(f'{len(people)} people remaining.')
            break
        elif not command == 'Paid':
            people.append(command)
        else:
            while people:
                print(people.popleft())


get_queue_lenght()
