def reverse_numbers():
    stack = list(map(int, input().split()))
    rev_numbers = [stack.pop() for num in range(len(stack))]
    print(' '.join(map(str, rev_numbers)))


reverse_numbers()
