def count_unique_numbers(numbers):
    num_occurrences_dict = {}
    for num in numbers.split():
        if num not in num_occurrences_dict:
            num_occurrences_dict[num] = 1
        else:
            num_occurrences_dict[num] += 1
    
    return num_occurrences_dict


def format_count_unique_numbers_output(count_numbers):
    count_numbers = {float(k): v for (k, v) in count_numbers.items()}
    for (k, v) in count_numbers.items():
        print(f'{k} - {v} times')


format_count_unique_numbers_output(count_unique_numbers(input()))
