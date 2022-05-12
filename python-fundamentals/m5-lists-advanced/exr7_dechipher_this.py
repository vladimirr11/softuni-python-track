message = input().split()


for word in message:
    digits = ''.join([ch for ch in word if ch.isnumeric()])

    if digits in word:
        chars = word.split(digits)
        chars = str(chars[1])
        replaced_digits = chr(int(digits))
        word = replaced_digits + chars

    word = ' '.join(word).split()
    word[1], word[-1] = word[-1], word[1]

    print(''.join(word), end=' ')
