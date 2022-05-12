number = int(input())


def make_loading_bar(number):
    time_loading_percents = number // 10
    pecrents = '%' * time_loading_percents
    points = '.' * ((100 - number) // 10)

    return f'{number}% [{pecrents}{points}]\nStill loading...'


if number == 100:
    print('100% Complete!\n[%%%%%%%%%%]')
else:
    print(make_loading_bar(number))
