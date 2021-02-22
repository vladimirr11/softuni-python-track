product = input()
city = input()

amount = float(input())

price = 0

if product == 'coffee' and city == 'Sofia':
    price = 0.50
elif product == 'water' and city == 'Sofia':
    price = 0.80
elif product == 'beer' and city == 'Sofia':
    price = 1.20
elif product == 'sweets' and city == 'Sofia':
    price = 1.45
elif product == 'peanuts' and city == 'Sofia':
    price = 1.60
elif product == 'coffee' and city == 'Plovdiv':
    price = 0.40
elif product == 'water' and city == 'Plovdiv':
    price = 0.70
elif product == 'beer' and city == 'Plovdiv':
    price = 1.15
elif product == 'sweets' and city == 'Plovdiv':
    price = 1.30
elif product == 'peanuts' and city == 'Plovdiv':
    price = 1.50
elif product == 'coffee' and city == 'Varna':
    price = 0.45
elif product == 'water' and city == 'Varna':
    price = 0.70
elif product == 'beer' and city == 'Varna':
    price = 1.10
elif product == 'sweets' and city == 'Varna':
    price = 1.35
elif product == 'peanuts' and city == 'Varna':
    price = 1.55


print(amount * price)