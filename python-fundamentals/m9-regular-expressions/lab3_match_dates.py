import re

dates = input()

patern = r'\b(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})\b'

for match in re.findall(patern, dates):
    day, separator, month, year = match
    print(f'Day: {day}, Month: {month}, Year: {year}')
