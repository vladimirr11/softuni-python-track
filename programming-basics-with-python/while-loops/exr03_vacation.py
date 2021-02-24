money_needed = float(input())
money_available = float(input())

waste_days = 0
counter = 1
saved_money = False

while waste_days < 5:
    spend_or_save = input()
    money_for_spend_or_save = float(input())
    if spend_or_save == 'spend':
        waste_days += 1
        if waste_days == 5:
            break
        money_available -= money_for_spend_or_save
        if money_for_spend_or_save > money_available:
            money_available = 0
    elif spend_or_save == 'save':
        money_available += money_for_spend_or_save
        if money_available >= money_needed:
            saved_money = True
            break

    counter += 1


if saved_money:
    print(f'You saved the money for {counter} days.')
else:
    print(f"You can't save the money.\n{counter}")