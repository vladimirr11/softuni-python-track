from itertools import permutations


def possible_permutations(lst: list):
    if len(lst) == 1:
        yield lst
    else:
        for per in permutations(lst):
            yield list(per)


if __name__ == '__main__':
    [print(n) for n in possible_permutations([1, 2, 3])]
