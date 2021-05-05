def repeat_by_lenght(word):
    """
    Repeat given word n-times depending on its lenght.
    """
    return word * len(word)


string_input: list = input().split()

print(''.join(map(repeat_by_lenght, string_input)))

# print(''.join(map(lambda word: word * len(word), string_input)))

# s = ''
# for word in string_input:
#     s += repeat_by_lenght(word)
#
# print(s)