import math

number_of_people = int(input())
capacity = int(input())

result = 0

if number_of_people % capacity == 0:
    result = int(number_of_people / capacity)
elif number_of_people % capacity > 0:
    result = math.ceil(number_of_people / capacity)
else:
    result = 1

print(result)