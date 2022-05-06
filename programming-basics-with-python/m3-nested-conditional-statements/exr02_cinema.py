service = input().capitalize()
rows = int(input())
columns = int(input())

income = rows * columns

if service == 'Premiere':
    income *= 12
    print(f'{income:.2f} leva')
elif service == 'Normal':
    income *= 7.5
    print(f'{income:.2f} leva')
elif service == 'Discount':
    income *= 5
    print(f'{income:.2f} leva')
