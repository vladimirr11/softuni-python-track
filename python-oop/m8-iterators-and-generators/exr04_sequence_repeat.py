class sequence_repeat:
    def __init__(self, seq, num) -> None:
        self.seq = seq
        self.num = num
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.num:
            curr_char = self.seq[self.counter % len(self.seq)]
            self.counter += 1            
            return curr_char
        
        raise StopIteration


if __name__ == '__main__':
    result = sequence_repeat("qwerty", 24)

    for item in result:
        print(item, end='')
