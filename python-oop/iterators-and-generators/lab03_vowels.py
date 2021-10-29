class vowels:
    def __init__(self, string) -> None:
        self.string = string 
        self.vowels = 'AaEeIiUuYyOo'
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.string):
            self.counter += 1
            if self.string[self.counter - 1] in self.vowels:
                return self.string[self.counter - 1]

        raise StopIteration


if __name__ == '__main__':
    my_string = vowels('Abcedifuty0o')

    for char in my_string:
        print(char)
