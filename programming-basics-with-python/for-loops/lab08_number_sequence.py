num = int(input())

biggest_num = 0
smallest_num = 0

for i in range(num):
    random_num = int(input())
    if i == 0:                        
        biggest_num = random_num
        smallest_num = random_num
    else:
        if random_num > biggest_num:
            biggest_num = random_num
        elif random_num < smallest_num:
            smallest_num = random_num

print(f'Max number: {biggest_num}\nMin number: {smallest_num}')