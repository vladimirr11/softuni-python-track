def expressions(numbers, current_result=0, current_expression=''):
    if not numbers:
        print(f'{current_expression}={current_result}')
        return 

    expressions(numbers[1:], current_result + numbers[0], f'{current_expression}+{numbers[0]}')
    expressions(numbers[1:], current_result - numbers[0], f'{current_expression}-{numbers[0]}')


nums = [int(x) for x in input().split(', ')]

expressions(nums)
