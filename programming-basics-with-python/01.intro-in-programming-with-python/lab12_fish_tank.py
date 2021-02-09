length_cm = int(input())
width_cm = int(input())
hight_cm = int(input())
occupied_volume = float(input())

total_volume = length_cm * width_cm * hight_cm
total_amount_liters = total_volume / 1000
procent_occupied_volume = occupied_volume / 100
real_amount_liters = total_amount_liters * (1-procent_occupied_volume)

print (f'{real_amount_liters:.3f}')