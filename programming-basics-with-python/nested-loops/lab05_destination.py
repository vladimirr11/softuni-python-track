destination = input()

while destination != 'End':
    amount_destination = float(input())
    saved_money = 0

    while amount_destination > saved_money:
        money_for_holiday = float(input())
        saved_money += money_for_holiday
        if saved_money >= amount_destination:
            print(f'Going to {destination}!')

    destination = input()