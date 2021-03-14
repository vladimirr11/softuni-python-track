first_list = input().split(', ')
second_list = input().split(', ')

my_list = []

for word in first_list:
    for word_two in second_list:
        if word in word_two:
            if word not in my_list:
                my_list.append(word)


print(my_list)