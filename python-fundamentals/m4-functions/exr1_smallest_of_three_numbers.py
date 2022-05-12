a = int(input())
b = int(input())
c = int(input())


def get_smallest_of_three_numbers(num_one, num_two, num_three):
    if num_one < num_two and num_one < num_three:
        return num_one
    elif num_two < num_one and num_two < num_three:
        return num_two
    else:
        return num_three


result = get_smallest_of_three_numbers(a, b, c)
print(result)
