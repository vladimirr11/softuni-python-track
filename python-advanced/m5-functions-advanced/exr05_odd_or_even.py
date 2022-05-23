def get_odd_or_even_sum(command, numbers):
    nums = [int(x) for x in numbers.split()]
    odd_sum, even_sum = (0, 0)
    if command == 'Odd':
        odd_nums = [n for n in nums if n % 2 != 0]
        odd_sum = sum(odd_nums) * len(nums)
        return odd_sum
    elif command == 'Even':
        even_nums = [n for n in nums if n % 2 == 0]
        even_sum = sum(even_nums) * len(nums)
        return even_sum


print(get_odd_or_even_sum(input(), input()))
