def print_min_max_and_sum_of_numbers(nums):
    print(f'The minimum number is {min(nums)}')
    print(f'The maximum number is {max(nums)}')
    print(f'The sum number is: {sum(nums)}')


print_min_max_and_sum_of_numbers(list(map(int, input().split())))
