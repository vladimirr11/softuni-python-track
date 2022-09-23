class countdown_iterator:
    def __init__(self, count) -> None:
        self.count = count
    
    def __iter__(self):
        return self
    
    def __next__(self):
        curr_count = self.count
        if curr_count >= 0:
            self.count -= 1
            return curr_count
        
        raise StopIteration


if __name__ == '__main__':
    iterator = countdown_iterator(10)

    for item in iterator:
        print(item, end=' ')
