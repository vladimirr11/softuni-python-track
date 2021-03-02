str_one = input()
str_two = input()

current_string = ''
previous_string = str_one

for iteration in range(len(str_one)):
    for index_str_two in range(0, iteration + 1):
        current_string += str_two[index_str_two]
        
    for index_str_one in range(iteration + 1, len(str_one)):
        current_string += str_one[index_str_one]

    if not previous_string == current_string:
        print(current_string)

    previous_string = current_string

    current_string = ''