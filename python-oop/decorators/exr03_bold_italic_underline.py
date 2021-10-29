def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<b>{result}</b>'
    
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<i>{result}</i>'
    
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f'<u>{result}</u>'
    
    return wrapper


if __name__ == '__main__':
    @make_bold
    @make_italic
    @make_underline
    def greet(*args):
        return f'Hello, {", ".join(args)}'

    print(greet('Peter', 'George'))
    