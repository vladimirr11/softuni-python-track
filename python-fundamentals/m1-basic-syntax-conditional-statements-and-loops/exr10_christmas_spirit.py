allowed_quantity_for_decoration = int(input())
days_until_christmas = int(input())

cristmas_spirit = 0
cost = 0

for i in range(1, days_until_christmas + 1):
    if i % 11 == 0:
        allowed_quantity_for_decoration += 2

    if i % 2 == 0:
        cost += allowed_quantity_for_decoration * 2
        cristmas_spirit += 5

    if i % 3 == 0:
        cost += allowed_quantity_for_decoration * 8
        cristmas_spirit += 13

    if i % 5 == 0:
        cost += allowed_quantity_for_decoration * 15
        cristmas_spirit += 17

    if i % 3 == 0 and i % 5 == 0:
        cristmas_spirit += 30

    if i % 10 == 0:
        cost += 23
        cristmas_spirit -= 20

    if i == days_until_christmas and i % 10 == 0:
        cristmas_spirit -= 30

print(f'Total cost: {cost}')
print(f'Total spirit: {cristmas_spirit}')
