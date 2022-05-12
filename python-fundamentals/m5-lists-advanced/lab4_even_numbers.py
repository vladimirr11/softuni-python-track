input_numbers = map(lambda x: int(x), input().split(', '))

even_numbers = [index for index, number in enumerate(input_numbers) if number % 2 == 0]

print(even_numbers)
