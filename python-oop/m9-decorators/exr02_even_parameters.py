def even_parameters(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                return 'Please use only even numbers!'
        result = func(*args, **kwargs)
        return result
    return wrapper


if __name__ == '__main__':
    @even_parameters
    def add(a, b):
        return a + b

    print(add(2, 4))

    print(add('Peter', 1))
