num = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(1, num + 1):
    ran_nums = int(input())
    if ran_nums % 2 == 0 and ran_nums % 3 == 0 and ran_nums % 4 == 0:
        p1 += 1
        p2 += 1
        p3 += 1
    elif ran_nums % 2 == 0 and ran_nums % 3 == 0:
        p1 += 1
        p2 += 1
    elif ran_nums % 2 == 0 and ran_nums % 4 == 0:
        p1 += 1
        p3 += 1
    elif ran_nums % 3 == 0 and ran_nums % 4 == 0:
        p2 += 1
        p3 += 1
    elif ran_nums % 2 == 0:
        p1 += 1
    elif ran_nums % 3 == 0:
        p2 += 1
    elif ran_nums % 4 == 0:
        p3 += 1


p1 = (p1 / num) * 100
p2 = (p2 / num) * 100
p3 = (p3 / num) * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')