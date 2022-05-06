word = input()

reversed_word = ''

for idx in range(len(word) - 1, -1, -1):
    reversed_word += word[idx]

print(reversed_word)
