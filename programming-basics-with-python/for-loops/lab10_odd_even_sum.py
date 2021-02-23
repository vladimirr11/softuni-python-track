num = int(input())

even = 0
odd = 0

for i in range(1, num + 1):
    element = int(input())
    if i % 2 == 0:
        even += element
    else:
        odd += element

if even == odd:
    print(f'Yes\nSum = {even}')
else:
    diff = abs(even - odd)
    print(f'No\nDiff = {diff}')