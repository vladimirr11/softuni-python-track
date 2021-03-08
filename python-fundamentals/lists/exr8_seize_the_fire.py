fire_cells = input().split('#')
water_amount = int(input())

effort = 0
my_list = []

for fire_cell in fire_cells:
    fire_type, _, fire_amount = fire_cell.split()
    fire_amount = int(fire_amount)

    if fire_type == 'High' and (81 <= fire_amount <= 125) and (water_amount - fire_amount >= 0):
        water_amount -= fire_amount
        effort += fire_amount * 0.25
        my_list.append(fire_amount)

    if fire_type == 'Medium' and (51 <= fire_amount <= 80) and (water_amount - fire_amount >= 0):
        water_amount -= fire_amount
        effort += fire_amount * 0.25
        my_list.append(fire_amount)

    if fire_type == 'Low' and (1 <= fire_amount <= 50) and (water_amount - fire_amount >= 0):
        water_amount -= fire_amount
        effort += fire_amount * 0.25
        my_list.append(fire_amount)


print('Cells:')
for item in my_list:
    print(f' - {item}')

print(f'Effort: {effort:.2f}')

total_sum = list(map(int, my_list))
print(f'Total Fire: {sum(total_sum)}')