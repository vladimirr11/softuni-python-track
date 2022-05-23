def sort_numbers(nums):
    return [int(x) for x in sorted(nums)]


print(sort_numbers(list(map(int, input().split()))))
