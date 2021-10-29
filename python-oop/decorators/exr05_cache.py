def cache(func):
    def wrapper(p):
        result = func(p)
        wrapper.log[p] = result

        return result

    wrapper.log = {}
    return wrapper


if __name__ == '__main__':
    @cache
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)


    fibonacci(4)
    print(fibonacci.log)
    