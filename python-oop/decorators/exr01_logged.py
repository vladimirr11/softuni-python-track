def logged(func):
    def wrapper(*args, ** kwargs):
        result = func(*args, **kwargs)

        return f'you called {func.__name__}({", ".join([str(arg) for arg in args])})\nit returned {result}'

    return wrapper


if __name__ == '__main__':
    @logged
    def sum_func(*args):
        return 3 + len(args)

    print(sum_func(4, 4, 4))
