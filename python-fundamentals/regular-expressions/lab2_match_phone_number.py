import re

numbers_input = input()

patern = r'(\+359\s2\s\d{3}\s\d{4}|\+359-2-\d{3}-\d{4})\b'

matches: list = re.findall(patern, numbers_input)

print(' '.join(matches))