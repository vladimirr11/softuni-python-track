class dictionary_iter:
    def __init__(self, dictionary) -> None:
        self.dictionary: dict = dictionary
        self._iter_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        idx = self._iter_idx
        if idx < len(self.dictionary):
            key = list(self.dictionary)[idx]
            value = self.dictionary[key]
            self._iter_idx += 1
            return key, value
        
        raise StopIteration


if __name__ == '__main__':
    result = dictionary_iter({1: "1", 2: "2"})

    for x in result:
        print(x)
