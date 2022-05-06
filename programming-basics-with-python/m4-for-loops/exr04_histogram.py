num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, num + 1):
    ran_nums = int(input())
    if ran_nums < 200:
        p1 += 1
    elif ran_nums < 400:
        p2 += 1
    elif ran_nums < 600:
        p3 += 1
    elif ran_nums < 800:
        p4 += 1
    elif ran_nums <= 1000:
        p5 += 1

p1 = (p1 / num) * 100
p2 = (p2 / num) * 100
p3 = (p3 / num) * 100
p4 = (p4 / num) * 100
p5 = (p5 / num) * 100


print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
