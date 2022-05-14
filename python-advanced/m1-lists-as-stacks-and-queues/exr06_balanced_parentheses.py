expression = input()

balanced = True
stack = []
for parenthesis in expression:
    if parenthesis in '{[(':
        stack.append(parenthesis)
    elif parenthesis in '})]':
        if not stack:
            balanced = False
            break

        opening_paran = stack.pop()

        if f'{opening_paran}{parenthesis}' not in ['[]', '{}', '()']:
            balanced = False
            break

if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')
