text = input()
num = 0

while text != 'Stop':
    current_int = int(text)
    num += current_int
    text = input()

print(num)
