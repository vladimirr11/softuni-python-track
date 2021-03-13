input_numbers = map(lambda x: int(x), input().split(', '))

even_numbers = [index for index, number in enumerate(input_numbers) if number % 2 == 0]

print(even_numbers)

# even_numbers = [index for index in range(len(input_numbers)) \
#             if input_numbers[index] % 2 == 0]

# print(list(filter(lambda n: n % 2 != 0, \ 
#            [i for i, n in enumerate(map(int, input().split(', ')))])))