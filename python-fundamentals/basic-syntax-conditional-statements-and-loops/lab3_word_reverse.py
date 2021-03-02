wrd = input()

reversed_wrd = ''

for char in range(len(wrd) - 1, -1, -1):
    reversed_wrd += wrd[char]

print(reversed_wrd)

# print(wrd[::-1])