num_days = int(input())
num_bakers = int(input())
num_cakes = int(input())
num_waffles = int(input())
num_pancakes = int(input())

sum_cake = num_cakes * 45
sum_waffles = num_waffles * 5.80
sum_pancakes = num_pancakes * 3.20
sum_for_a_day = (sum_cake + sum_waffles + sum_pancakes) * num_bakers
total_money = sum_for_a_day * num_days
real_money = total_money - (total_money / 8)

print(f'{real_money:.2f}')