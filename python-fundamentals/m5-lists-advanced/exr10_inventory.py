collected_items = input().split(', ')


while True:
    command = input().split(' - ')
    if command[0] == 'Craft!':
        break

    if command[0] == 'Collect':
        item = command[1]

        if item not in collected_items:
            collected_items.append(item)

    if command[0] == 'Drop':
        item = command[1]

        if item in collected_items:
            collected_items.remove(item)

    if command[0] == 'Combine Items':
        old_item, new_item = command[1].split(':')

        if old_item in collected_items:
            for index, value in enumerate(collected_items):
                if value == old_item:
                    collected_items.insert(index + 1, new_item)

    if command[0] == 'Renew':
        item = command[1]

        if item in collected_items:
            collected_items.remove(item)
            collected_items.append(item)


print(', '.join(collected_items))
