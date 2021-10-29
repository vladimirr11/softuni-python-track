def find_stronger_numbers(numbers):
    """
    """
    lst_of_numbers = [int(num) for num in numbers.split()]

    negative_numbers = []
    positive_numbers = []
    for num in lst_of_numbers:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)

    print(f'-{sum(list(map(abs, negative_numbers)))}')
    print(sum(positive_numbers))
    if sum(list(map(abs, negative_numbers))) > sum(positive_numbers):
        print(f'The negatives are stronger than the positives')
    else:
        print(f'The positives are stronger than the negatives')


find_stronger_numbers(input())
