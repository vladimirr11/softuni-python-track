def read_next(*args):
    for curr_iter in args:
        for el in range(len(curr_iter)):
            if isinstance(curr_iter, dict):
                yield list(curr_iter.keys())[el]
                continue
            yield curr_iter[el]


if __name__ == '__main__':
    for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
        print(item, end='')
