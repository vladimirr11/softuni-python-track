n = int(input())

stack = []
for i in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack:
            stack.pop()
    elif command[0] == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))


reveresed_elemens = []
for i in range(len(stack)):
    reveresed_elemens.append(stack.pop())


print(', '.join(map(str, reveresed_elemens)))
