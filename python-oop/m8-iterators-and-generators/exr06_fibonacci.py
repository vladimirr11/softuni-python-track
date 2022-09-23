def fibonacci():
    fb_0, fb_1 = 0, 1
    yield fb_0
    yield fb_1
    fn_1, fn_2 = fb_1, fb_0

    while True:
        fn = fn_1 + fn_2
        yield fn

        fn_2, fn_1 = fn_1, fn


if __name__ == '__main__':
    generator = fibonacci()

    for i in range(5):
        print(next(generator))
