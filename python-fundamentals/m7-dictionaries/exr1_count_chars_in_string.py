string_input = input().split(' ')

my_dict = {}

for word in string_input:
    for char in word:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1

for k, v in my_dict.items():
    print(f'{k} -> {v}')
