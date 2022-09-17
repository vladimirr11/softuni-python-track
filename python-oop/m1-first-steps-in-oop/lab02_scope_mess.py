x = 'global'


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    def change_global():
        global x
        x = 'global: changed!'
        print(x)

    print('outer:', x)
    inner()
    print('outer:', x)
    change_global()


if __name__ == '__main__':
    print(x)
    outer()
