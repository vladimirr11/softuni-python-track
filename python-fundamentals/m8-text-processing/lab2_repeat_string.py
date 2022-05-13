def repeat_by_lenght(word):
    """
    Repeat given word n-times depending on its lenght.
    """
    return word * len(word)


string_input: list = input().split()

print(''.join(map(repeat_by_lenght, string_input)))
