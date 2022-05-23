def get_even_numbers(nums):
    return [int(num) for num in filter(lambda even: int(even) % 2 == 0, nums.split())]


print(get_even_numbers(input()))
