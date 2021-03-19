products = input().split(' ')
searched_products = input().split(' ')

bakery = {}

for index in range(0, len(products), 2):
    product_name = products[index]
    product_quantity = products[index + 1]
    bakery[product_name] = int(product_quantity)

for searched_product in searched_products:
    if searched_product in bakery:
        print(f'We have {bakery[searched_product]} of {searched_product} left')
    else:
        print(f'Sorry, we don\'t have {searched_product}')