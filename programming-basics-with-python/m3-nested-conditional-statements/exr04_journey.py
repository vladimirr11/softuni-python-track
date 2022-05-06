budget = float(input())
season = input()

destination = ''
holiday = ''
spend_money = 0

if budget <= 100 and season == 'summer':
    destination = 'Bulgaria'
    holiday = 'Camp'
    spend_money = budget * 0.3
elif budget <= 100 and season == 'winter':
    destination = 'Bulgaria'
    holiday = 'Hotel'
    spend_money = budget * 0.7
elif budget <= 1000 and season == 'summer':
    destination = 'Balkans'
    holiday = 'Camp'
    spend_money = budget * 0.4
elif budget <= 1000 and season == 'winter':
    destination = 'Balkans'
    holiday = 'Hotel'
    spend_money = budget * 0.8
elif budget > 1000 and season == 'summer':
    destination = 'Europe'
    holiday = 'Hotel'
    spend_money = budget * 0.9
elif budget > 1000 and season == 'winter':
    destination = 'Europe'
    holiday = 'Hotel'
    spend_money = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{holiday} - {spend_money:.2f}')
