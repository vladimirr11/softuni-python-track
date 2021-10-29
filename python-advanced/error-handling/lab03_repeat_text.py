try:
    text = input()
    repeats_text = int(input())
    print(text * repeats_text)
except ValueError:
    print('Varible times must be an intiger')
    