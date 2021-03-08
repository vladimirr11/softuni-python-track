gifts = input().split()


while True:
    command = input()
    if command == 'No Money':
        break

    command = command.split()

    if command[0] == 'Required':
        possition = int(command[2])
        if possition >= len(gifts) or possition < 0:
            continue
        gifts[possition] = command[1]
    
    if command[0] == 'OutOfStock':
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = None
    
    if command[0] == 'JustInCase':
        gifts[-1] = command[1]


for item in gifts:
    if item != None:
        print(item, end = ' ')