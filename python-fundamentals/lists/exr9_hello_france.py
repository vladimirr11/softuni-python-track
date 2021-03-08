item_price_pairs = input().split('|')
budget = float(input())

new_budget = budget
my_list = []
ADDED_VALUE = 0.4
TICKETS = 150

for pair in item_price_pairs:
    item_type, price = pair.split('->')
    price = float(price)

    if item_type == 'Clothes' and price <= 50. and new_budget >= price:
        new_budget -= price
        new_price = price + price * ADDED_VALUE
        my_list.append(new_price)
    
    if item_type == 'Shoes' and price <= 35. and new_budget >= price:
        new_budget -= price
        new_price = price + price * ADDED_VALUE
        my_list.append(new_price)
    
    if item_type == 'Accessories' and price <= 20.5 and new_budget >= price:
        new_budget -= price
        new_price = price + price * ADDED_VALUE
        my_list.append(new_price)


for item in my_list:
    print(f'{item:.2f}', end = ' ')

profit = (budget - new_budget) * ADDED_VALUE 

print()
print(f'Profit: {profit:.2f}')

selled_items = sum(list(map(float, my_list)))
total_money = selled_items + new_budget

if TICKETS >= total_money:
    print('Time to go.')
else:
    print('Hello, France!')