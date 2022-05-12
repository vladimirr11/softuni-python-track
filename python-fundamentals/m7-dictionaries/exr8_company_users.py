my_dict = {}

while True:
    company_users = input()
    if company_users == 'End':
        break

    company, id = company_users.split(' -> ')

    if company not in my_dict:
        my_dict[company] = []

    if id not in my_dict[company]:
        my_dict[company].append(id)


sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (x[0], x[1])))

for k, v in sorted_dict.items():
    print(k)
    for id in v:
        print(f'-- {id}')
