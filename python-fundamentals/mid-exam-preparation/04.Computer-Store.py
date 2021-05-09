total_price = 0

while True:
    order = input()
    if order == 'special' or order == 'regular':
        break

    prices = float(order)

    if prices <= 0:
        print('Invalid price!')

    if prices > 0:
        total_price += prices


tax = total_price * 0.2
final_price = total_price + tax


if total_price == 0:
    print('Invalid order!')
else:
    if order == 'special':
        final_price *= 0.9
        print(f"""
Congratulations you've just bought a new computer!
Price without taxes: {total_price:.2f}$
Taxes: {tax:.2f}$
-----------
Total price: {final_price:.2f}$""")
    else:
        print(f"""
Congratulations you've just bought a new computer!
Price without taxes: {total_price:.2f}$
Taxes: {tax:.2f}$
-----------
Total price: {final_price:.2f}$""")