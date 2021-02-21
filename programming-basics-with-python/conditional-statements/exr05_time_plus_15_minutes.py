hours = int(input())
minutes = int(input())


if hours <= 23 and minutes <= 44:
    print(f'{hours}:{minutes + 15}')
elif hours < 23 and 44 < minutes < 55:
    minutes += 15
    minutes %= 60
    print(f'{hours +1}:0{minutes}')
elif hours < 23 and 54 < minutes <= 59:
    minutes += 15
    minutes %= 60
    print(f'{hours + 1}:{minutes}')
elif hours == 23 and 44 < minutes < 55:
    minutes += 15
    minutes %= 60
    print(f'0:0{minutes}')
elif hours == 23 and 54 < minutes <= 59:
    minutes += 15
    minutes %= 60
    print(f'0:{minutes}')