MAX_NUM = 100
MIN_NUM = 1

while True:
    num = float(input())
    if MIN_NUM <= num <= MAX_NUM:
        print(f'The number {num} is between {MIN_NUM} and {MAX_NUM}')
        break