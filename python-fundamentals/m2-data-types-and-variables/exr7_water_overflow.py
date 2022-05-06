CAPACITY = 255

number_of_lines = int(input())

total_liters_in_the_tank = 0

for line in range(number_of_lines):
    quantity = int(input())
    total_liters_in_the_tank += quantity

    if quantity > CAPACITY:
        print(f'Insufficient capacity!')
        CAPACITY += quantity
        total_liters_in_the_tank -= quantity

    CAPACITY -= quantity

print(total_liters_in_the_tank)
