def reverse_string(text):
    """
    """
    stack = [char for char in text]

    reversed_text = []
    while stack:
        reversed_text.append(stack.pop())

    # return text[::-1]
    return reversed_text


print(''.join(reverse_string(input())))
