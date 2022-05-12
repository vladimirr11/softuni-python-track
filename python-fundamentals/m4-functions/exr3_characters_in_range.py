ch_one = input()
ch_two = input()


def get_ascii_charaters(char_one, char_two):
    result = []
    for r in range(ord(char_one) + 1, ord(char_two)):
        result.append(chr(r))

    return ' '.join(result)


res = get_ascii_charaters(ch_one, ch_two)
print(res)
