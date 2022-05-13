sugar_cubes = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == 'Mort':
        break

    if command[0] == 'Add':
        value = int(command[1])
        sugar_cubes.append(value)

    if command[0] == 'Remove':
        value = int(command[1])
        if value in sugar_cubes:
            sugar_cubes.remove(value)

    if command[0] == 'Replace':
        value = int(command[1])
        replacement = int(command[2])
        poss = 0

        for i in range(len(sugar_cubes)):
            if sugar_cubes[i] == value:
                poss = i
                break
        sugar_cubes.insert(poss, replacement)
        sugar_cubes.remove(value)

    if command[0] == 'Collapse':
        value = int(command[1])

        sugar_cubes = [el for el in sugar_cubes if el >= value]

sugar_cubes = list(map(str, sugar_cubes))
print(' '.join(sugar_cubes))
