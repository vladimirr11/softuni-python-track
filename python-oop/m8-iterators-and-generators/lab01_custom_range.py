class custom_range:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.counter = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.stop:
            self.counter += 1
            return self.counter
        
        raise StopIteration


if __name__ == '__main__':
    one_to_ten = custom_range(1, 10)

    for num in one_to_ten:
        print(num)
        