class take_skip:
    def __init__(self, step, count) -> None:
        self.step = step
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_count < (self.count * self.step):
            curr_step = self.current_count
            self.current_count += self.step
            return curr_step
        
        raise StopIteration


if __name__ == '__main__':
    numbers = take_skip(10, 5)
    
    for number in numbers:
        print(number)
        