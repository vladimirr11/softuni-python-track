num = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(num):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)

count_positive_numbers = len(positive_numbers)
sum_negative_numbers = sum(negative_numbers)

print(positive_numbers)
print(negative_numbers)

print(
    f'Count of positives: {count_positive_numbers}. Sum of negatoves: {sum_negative_numbers}')
