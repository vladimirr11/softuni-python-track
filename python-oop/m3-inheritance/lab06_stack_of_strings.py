class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f'[{", ".join(self.data[::-1])}]'


if __name__ == '__main__':
    stack = Stack()

    stack.push('apple')
    stack.push('carrot')
    print(stack)
    stack.pop()
    print(stack.is_empty())
