first_number = int(input())
second_number = int(input())

result = []

for i in range(1, second_number + 1):
    result.append(first_number * i)

print(result)