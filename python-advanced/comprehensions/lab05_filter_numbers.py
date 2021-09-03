def filter_numbers(start_num, end_num):
    """
    """
    filtered_numbers = [num for num in range(start_num, end_num + 1)  \
        if any([num % x == 0 for x in range(2, 11)])]

    return filtered_numbers


print(filter_numbers(int(input()), int(input())))
