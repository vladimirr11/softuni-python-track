from collections import deque


chocos = deque(map(int, input().split(', ')))
cups_of_milks = deque(map(int, input().split(', ')))

made_shakes = 0
while True:
    if made_shakes == 5 or len(chocos) == 0 or len(cups_of_milks) == 0:
        break

    choco = chocos.pop()
    cup_of_milk = cups_of_milks.popleft()

    if choco <= 0:
        cups_of_milks.appendleft(cup_of_milk)
        continue

    if cup_of_milk <= 0:
        chocos.append(choco)
        continue

    if choco == cup_of_milk:
        made_shakes += 1
        continue
    else:
        cups_of_milks.append(cup_of_milk)
        choco -= 5
        if choco <= 0:
            continue
        chocos.append(choco)


chocos_lst = list(chocos)
milks_lst = list(cups_of_milks)


if made_shakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if len(chocos_lst) > 0:
    print(f'Chocolate: {", ".join(list(map(str, chocos_lst)))}')
else:
    print('Chocolate: empty')

if len(milks_lst) > 0:
    print(f'Milk: {", ".join(list(map(str, milks_lst)))}')
else:
    print('Milk: empty')
