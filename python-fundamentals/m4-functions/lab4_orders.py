order = input()
quantity = int(input())


def calculate_total_price(product: str, quantity: int):
    result = None

    if product == 'coffee':
        result = 1.5 * quantity
    if product == 'water':
        result = 1.0 * quantity
    if product == 'coke':
        result = 1.4 * quantity
    if product == 'snacks':
        result = 2.0 * quantity

    return f'{result:.2f}'


print(calculate_total_price(order, quantity))
