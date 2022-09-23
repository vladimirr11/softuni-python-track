class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.reverse_iter_len = len(iterable)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.reverse_iter_len > 0:
            self.reverse_iter_len -= 1
            return self.iterable[self.reverse_iter_len]
        
        raise StopIteration


if __name__ == '__main__':
    reversed_list = reverse_iter([1, 2, 3, 4])

    for item in reversed_list:
        print(item)
