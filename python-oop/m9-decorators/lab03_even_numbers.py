def even_numbers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        even_nums = [num for num in result if num % 2 == 0]
        return even_nums

    return wrapper


if __name__ == '__main__':
    @even_numbers
    def get_numbers(numbers):
        return numbers

    print(get_numbers([1, 2, 3, 4, 5]))
