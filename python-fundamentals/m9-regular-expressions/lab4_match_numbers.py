import re

string_input = input()

patern = r'(((^|(?<=\s))(-*)(\d+))((\.\d+)*)($|(?=\s)))'

for match in re.findall(patern, string_input):
    number, *others = match
    print(number, end=' ')
