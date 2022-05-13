import re

num_lines = int(input())

regex = r'^([$%])[A-Z][a-z][a-z]+\1:\s\[\d+]\|\[\d+]\|\[\d+]\|$'

for line in range(num_lines):
    message = input()
    if re.match(regex, message):
        tag = re.findall(r'[A-Z][a-z]+', message)
        digits = re.findall(r'\d+', message)
        digits = list(map(int, digits))
        decrypted_message = [chr(digit) for digit in digits]
        decrypted_message = ''.join(decrypted_message)
        print(f'{tag[0]}: {decrypted_message}')
    else:
        print(f'Valid message not found!')
