numbers = [int(x) for x in input().split(', ')]


def sort_numbers(numbers):
    possitive = [x for x in numbers if x >= 0]
    negative = [x for x in numbers if x < 0]
    even = [x for x in numbers if x % 2 == 0]
    odd = [x for x in numbers if x % 2 != 0]

    return (possitive, negative, even, odd)


possitive, negative, even, odd = sort_numbers(numbers)

print(f'Positive:', ', '.join([str(x) for x in possitive]))
print(f'Negative:', ', '.join([str(x) for x in negative]))
print(f'Even:', ', '.join([str(x) for x in even]))
print(f'Odd:', ', '.join([str(x) for x in odd]))
