targets = list(map(int, input().split()))


while True:
    command = input().split()
    if command[0] == 'End':
        break

    if command[0] == 'Shoot':
        index = int(command[1])
        value = int(command[2])

        if len(targets) > index and targets[index] >= value:
            targets[index] -= value

        if len(targets) > index and targets[index] < value:
            targets.pop(index)

    if command[0] == 'Add':
        index = int(command[1])
        value = int(command[2])

        if len(targets) > index:
            targets.insert(index, value)

        if len(targets) <= index:
            print('Invalid placement!')

    if command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])

        left_radius = targets[:index]
        right_radius = targets[index:]

        if len(left_radius) >= radius and len(right_radius) >= radius:
            beginnig = index - radius
            end = index + radius
            targets = targets[:beginnig] + targets[end + 1:]
        else:
            print('Strike missed!')


targets = list(map(str, targets))
print('|'.join(targets))
