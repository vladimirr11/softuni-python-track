def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for i in integers():
            yield i / 2
    
    def take(n, seq):
        seq_list = []

        for el in seq:
            if len(seq_list) == n:
                return seq_list
            else:
                seq_list.append(el)
    
    return (take, halves, integers)

    
if __name__ == '__main__':
    take = solution()[0]
    halves = solution()[1]

    print(take(5, halves()))
    