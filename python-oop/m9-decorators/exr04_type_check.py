def type_check(type):
    def decorator(func):
        def wrapper(param):
            if isinstance(param, type):
                result = func(param)
                return result
            return 'Bad Type'
        return wrapper
    return decorator


if __name__ == '__main__':
    @type_check(int)
    def times2(num):
        return num * 2

    print(times2(2)) 
    print(times2('Not A Number'))
