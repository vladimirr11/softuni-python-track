#  program that sums vowels letters in a given text
text = input()

converted_char = 0

for char in text:
    if char == 'e':
        converted_char += 2
    elif char == 'a':
        converted_char += 1
    elif char == 'i':
        converted_char += 3
    elif char == 'o':
        converted_char += 4
    elif char == 'u':
        converted_char += 5

print(converted_char)
