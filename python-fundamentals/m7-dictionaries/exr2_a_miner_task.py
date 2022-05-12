my_dict = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in my_dict:
        my_dict[resource] = 0

    my_dict[resource] += quantity

for k, v in my_dict.items():
    print(f'{k} -> {v}')
