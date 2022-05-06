age = int(input())
washing_machine_price = float(input())
sum_toys = int(input())

birthday_money = 0
num_toys = 0
saved_money_birthday = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        birthday_money += 10
        saved_money_birthday += birthday_money - 1
    else:
        num_toys += sum_toys

saved_money = saved_money_birthday + num_toys

if saved_money >= washing_machine_price:
    diff = saved_money - washing_machine_price
    print(f'Yes! {diff:.2f}')
else:
    diff = washing_machine_price - saved_money
    print(f'No! {diff:.2f}')
