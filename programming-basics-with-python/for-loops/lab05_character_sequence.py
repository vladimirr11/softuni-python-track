# program that read text and prints every character of a new line

text = input()

for index, char in enumerate(text):
    print(index, char)