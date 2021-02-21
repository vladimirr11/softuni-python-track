budget = float(input())
num_people = int(input())
price_clothing = float(input())

setting = budget * 0.1

if num_people < 150:
    expenses = (num_people * price_clothing) + setting
    if expenses > budget:
        print(f'Not enough money!')
        print(f'Wingard needs {abs(expenses - budget):.2f} leva more.')
    else:
        print(f'Action!')
        print(f'Wingard starts filming with {abs(expenses - budget):.2f} leva left.')
else:
    price_clothing *= 0.9
    expenses = (num_people * price_clothing) + setting
    if expenses > budget:
        print(f'Not enough money!')
        print(f'Wingard needs {abs(expenses - budget):.2f} leva more.')
    else:
        print(f'Action!')
        print(f'Wingard starts filming with {abs(expenses - budget):.2f} leva left.')