num_tabs = int(input())
salary = float(input())

fine = 0

for i in range(1, num_tabs + 1):
    open_tabs = input()
    if open_tabs == 'Facebook':
        fine += 150
        if fine >= salary:
            print(f'You have lost your salary.')
            break
    elif open_tabs == 'Instagram':
        fine += 100
        if fine >= salary:
            print(f'You have lost your salary.')
            break
    elif open_tabs == 'Reddit':
        fine += 50
        if fine >= salary:
            print(f'You have lost your salary.')
            break

if fine < salary:
    left_money = salary - fine
    print(round(left_money))