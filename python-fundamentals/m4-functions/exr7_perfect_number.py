number = int(input())


def get_perfect_number(number):
    my_list = [n for n in range(1, number + 1) if number % n == 0]

    sum_numbers = 0
    for i in my_list[:-1]:
        sum_numbers += i

    return 'We have a perfect number!' if sum_numbers == number else 'It\'s not so perfect.'


print(get_perfect_number(number))
