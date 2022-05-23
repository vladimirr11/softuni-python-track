def even_odd(*args):
    nums, cmd = args[:-1], args[-1]
    odd_nums = [int(n) for n in nums if n % 2 != 0]
    even_nums = [int(n) for n in nums if n % 2 == 0]

    return odd_nums if cmd == 'odd' else even_nums


print(even_odd(1, 2, 3, 4, 5, 6, 'even'))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'odd'))
