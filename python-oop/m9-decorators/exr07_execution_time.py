import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        stop = time.time()
        return stop - start
    return wrapper


if __name__ == '__main__':
    @exec_time
    def concatenate(strings):
        result = ""
        for string in strings:
            result += string
        return result

    print(concatenate(["a" for i in range(1000000)]))
