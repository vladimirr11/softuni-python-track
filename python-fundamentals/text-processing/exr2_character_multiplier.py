words = input().split()

first_word = words[0]
second_word = words[1]

min_lenght = min(len(first_word), len(second_word))

total_sum = 0
for i in range(min_lenght):
    total_sum += ord(first_word[i]) * ord(second_word[i])

longer_word = first_word

if len(second_word) > len(first_word):
    longer_word = second_word

for i in range(min_lenght, len(longer_word)):
    total_sum += ord(longer_word[i])

print(total_sum)