def multiply(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, *kwargs)
            return result * n
        return wrapper
    return decorator


if __name__ == '__main__':
    @multiply(3)
    def add_ten(number):
        return number + 10

    print(add_ten(3))   
