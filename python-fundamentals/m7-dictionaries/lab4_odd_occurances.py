input_string = input().split(' ')

my_dict = {}

for word in input_string:
    if word.lower() in my_dict:
        my_dict[word.lower()] += 1
    else:
        my_dict[word.lower()] = 1

print(' '.join([v for v, k in my_dict.items() if k % 2 == 1]))
