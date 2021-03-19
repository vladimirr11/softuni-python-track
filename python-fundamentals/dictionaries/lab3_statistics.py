products = {}

while True:
    input_product = input()
    if input_product == 'statistics':
        break
    
    product_name, product_quantity = input_product.split(': ')
    if product_name in products:
        products[product_name] += int(product_quantity)
    else:
        products[product_name] = int(product_quantity)

print('Products in stock:')    
for k, v in products.items():
    print(f'- {k}: {v}')
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')