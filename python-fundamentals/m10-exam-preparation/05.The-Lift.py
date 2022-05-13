number_of_people = int(input())
lift_wagons = list(map(int, input().split()))

WAGON_CAPACITY = 4

for wagon_index in range(len(lift_wagons)):
    while not lift_wagons[wagon_index] == WAGON_CAPACITY:
        if number_of_people > 0:
            lift_wagons[wagon_index] += 1
            number_of_people -= 1
        else:
            break

unoccupaid_wagons = False

for wagon in lift_wagons:
    if wagon < 4:
        unoccupaid_wagons = True

if number_of_people == 0 and unoccupaid_wagons == True:
    print('The lift has empty spots!')
    print(' '.join(list(map(str, lift_wagons))))

if number_of_people > 0 and unoccupaid_wagons == False:
    print(f'There isn\'t enough space! {number_of_people} people in a queue!')
    print(' '.join(list(map(str, lift_wagons))))

if number_of_people == 0 and unoccupaid_wagons == False:
    print(' '.join(list(map(str, lift_wagons))))
