from math import pi

figure = input()
area = 0
is_valid = True


if figure == 'square':
    length_sq = float(input())
    area = length_sq * length_sq
elif figure == 'rectangle':
    length_rec_one = float(input())
    length_rec_two = float(input())
    area = length_rec_one * length_rec_two
elif figure == 'circle':
    rad_circle = float(input())
    area = pi * (rad_circle * rad_circle)
elif figure == 'triangle':
    length_triang = float(input())
    height = float(input())
    area = (length_triang * height) / 2
else:
    print('Not a correct figure!')
    is_valid = False


if is_valid:
    print(f'{area:.3f}')