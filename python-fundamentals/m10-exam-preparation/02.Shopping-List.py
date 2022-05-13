groceries = input().split('!')

while True:
    command = input().split()
    if command[0] == 'Go' and command[1] == 'Shopping!':
        break

    if command[0] == 'Urgent':
        item = command[1]
        if item not in groceries:
            groceries.insert(0, item)

    if command[0] == 'Unnecessary':
        item = command[1]
        if item in groceries:
            groceries.remove(item)

    if command[0] == 'Correct':
        old_item = command[1]
        new_item = command[2]

        if old_item in groceries:
            for i, v in enumerate(groceries):
                if v == old_item:
                    groceries[i] = new_item

    if command[0] == 'Rearrange':
        item = command[1]

        if item in groceries:
            groceries.remove(item)
            groceries.append(item)


print(', '.join(groceries))
