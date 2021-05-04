my_dict = {}
product_prices_dict = {}

while True:
    string_input = input()
    if string_input == 'buy':
        break

    product, price, quantity = string_input.split()

    if product not in my_dict or product not in product_prices_dict:
        my_dict[product] = 0
        product_prices_dict[product] = 0

    my_dict[product] += int(quantity)
    product_prices_dict[product] = float(price)


for key, value in my_dict.items():
    print(f'{key} -> {value * product_prices_dict[key]:.2f}')