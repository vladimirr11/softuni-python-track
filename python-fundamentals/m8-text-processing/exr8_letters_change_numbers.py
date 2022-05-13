input_string = input().split()

total_sum = 0

for string in input_string:
    if string[0].isupper():
        index = 1
        digits = ''
        fst_letter = ord(string[0]) - 64

        while string[index].isdigit():
            digits += string[index]
            index += 1

        digits = int(digits)

        total_sum += digits / fst_letter

        if string[-1].isupper():
            last_letter = ord(string[-1]) - 64

            total_sum -= last_letter

        if string[-1].islower():
            last_letter = ord(string[-1]) - 96

            total_sum += last_letter

    if string[0].islower():
        index = 1
        digits = ''
        fst_letter = ord(string[0]) - 96

        while string[index].isdigit():
            digits += string[index]
            index += 1

        digits = int(digits)

        total_sum += digits * fst_letter

        if string[-1].isupper():
            last_letter = ord(string[-1]) - 64

            total_sum -= last_letter

        if string[-1].islower():
            last_letter = ord(string[-1]) - 96

            total_sum += last_letter


print(f'{total_sum:.2f}')
