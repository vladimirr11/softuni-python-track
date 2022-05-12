number = input()


def get_even_and_odd_sum(number):
    sum_odd = 0
    sum_even = 0

    for digit in number:
        if int(digit) % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


print(get_even_and_odd_sum(number))
