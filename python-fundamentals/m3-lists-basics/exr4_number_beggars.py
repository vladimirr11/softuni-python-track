string_numbers = input().split(', ')
num_beggars = int(input())

result = []

for beggar in range(1, num_beggars + 1):
    sum_stolen_items = 0
    for item in range(beggar - 1, len(string_numbers), num_beggars):
        sum_stolen_items += int(string_numbers[item])
    result.append(sum_stolen_items)

print(result)
