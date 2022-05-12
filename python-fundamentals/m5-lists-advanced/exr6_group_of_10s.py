list_of_numbers = list(map(int, input().split(', ')))

for max_value in range(10, 101, 10):
    initial_value = 0
    result = list(filter(lambda x: initial_value <= x <= max_value, list_of_numbers))
    list_of_numbers = [elem for elem in list_of_numbers if elem not in result]
    print(f'Group of {max_value}\'s: {result}')
    if list_of_numbers == []:
        break

    initial_value += 10
