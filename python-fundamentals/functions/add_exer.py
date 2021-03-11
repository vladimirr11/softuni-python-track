collection_of_items = input()
budget = float(input())

bought_products = []
new_prices = []

for item in collection_of_items.split('|'):
    tokens = item.split('->')
    type_of_product = tokens[0]
    price_of_product = tokens[1]
    if type_of_product == 'Clothes' and price_of_product > 50.0:
        continue
    if type_of_product == 'Shoes' and price_of_product > 35.0:
        continue    
    if type_of_product == 'Accessories' and price_of_product > 20.5:
        continue
    
    if budget > price_of_product:
        budget -= price_of_product
        bought_products.append(price_of_product)
        new_prices.append(price_of_product * 1.4)


for new_price in new_prices:
    print(f'{new_price:.2f}', end = ' ')
print('')

profit = sum(new_prices) - sum(bought_products)
print(f'Profit: {profit:.2f}')

new_budget = profit + sum(new_prices)
if new_budget >= 150:
    print('Hello France!')
else:
    print('Time to go.')