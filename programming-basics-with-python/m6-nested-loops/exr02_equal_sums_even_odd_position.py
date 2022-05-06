first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    num_to_str = str(i)
    even_num = 0
    odd_num = 0

    for index, digit in enumerate(num_to_str):
        if index % 2 == 0:
            even_num += int(digit)
        else:
            odd_num += int(digit)

    if even_num == odd_num:
        print(i, end=' ')
