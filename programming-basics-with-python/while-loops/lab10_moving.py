width = int(input())
length = int(input())
height = int(input())

cubic_area = width * length * height
num_carton = 0

while num_carton <= cubic_area:
    cartons = input()
    if cartons == 'Done':
        break

    var = int(cartons)
    num_carton += var


if num_carton > cubic_area:
    diff = abs(cubic_area - num_carton)
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    diff = abs(cubic_area - num_carton)
    print(f'{diff} Cubic meters left.')