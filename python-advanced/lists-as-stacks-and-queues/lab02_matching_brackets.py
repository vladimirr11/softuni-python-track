def match_brackets(expression):
    """
    """
    brackets_stack = []
    sub_expressions = []

    for idx in range(len(expression)):
        if expression[idx] == '(':
            brackets_stack.append(idx)
        elif expression[idx] == ')':
            start_index = brackets_stack.pop()
            sub_expressions.append(expression[start_index:idx + 1])

    return sub_expressions


for exp in match_brackets(input()):
    print(exp)
