numbers_list = input().split(', ')

result = 0

for i in range(len(numbers_list)):
    result += int(numbers_list[i])

print(result)
