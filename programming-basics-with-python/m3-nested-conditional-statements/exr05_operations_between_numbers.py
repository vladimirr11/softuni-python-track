number1 = int(input())
number2 = int(input())
symbol = input()

result = 0

if symbol == '+':
    result = number1 + number2
    even_odd = (number1 + number2) % 2
    if even_odd == 0:
        print(f'{number1} {symbol} {number2} = {result} - even')
    else:
        print(f'{number1} {symbol} {number2} = {result} - odd')

elif symbol == '-':
    result = number1 - number2
    even_odd = (number1 - number2) % 2
    if even_odd == 0:
        print(f'{number1} {symbol} {number2} = {result} - even')
    else:
        print(f'{number1} {symbol} {number2} = {result} - odd')

elif symbol == '*':
    result = number1 * number2
    even_odd = (number1 * number2) % 2
    if even_odd == 0:
        print(f'{number1} {symbol} {number2} = {result} - even')
    else:
        print(f'{number1} {symbol} {number2} = {result} - odd')

elif symbol == '/':
    if number2 == 0:
        print(f'Cannot divide {number1} by zero')
    else:
        result = number1 / number2
        print(f'{number1} {symbol} {number2} = {result:.2f}')

elif symbol == '%':
    if number2 == 0:
        print(f'Cannot divide {number1} by zero')
    else:
        result = number1 % number2
        print(f'{number1} {symbol} {number2} = {result}')
