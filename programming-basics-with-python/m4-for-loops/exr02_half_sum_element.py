import sys

num = int(input())

max_num = -sys.maxsize
sum_rand_num = 0

for i in range(0, num):
    random_num = int(input())
    if max_num < random_num:
        max_num = random_num
    sum_rand_num += random_num

if max_num == sum_rand_num - max_num:
    print(f'Yes\nSum = {max_num}')
else:
    diff = abs(max_num - (sum_rand_num - max_num))
    print(f'No\nDiff = {diff}')
