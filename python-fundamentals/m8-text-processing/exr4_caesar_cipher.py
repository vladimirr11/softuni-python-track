string_input = input()

chiphered_string = ''

for ch in string_input:
    shifthed_ascii = ord(ch) + 3
    chiphered_string += chr(shifthed_ascii)

print(chiphered_string)
