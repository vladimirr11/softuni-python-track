my_dict = {}

while True:
    forcebook = input()
    if forcebook == 'Lumpawaroo':
        break

    if '|' in forcebook:

        force_side, force_user = forcebook.split(' | ')

        if force_side not in my_dict:
            my_dict[force_side] = []

        handle = False
        for k, v in my_dict.items():
            if force_user in v:
                handle = True

        if force_user not in my_dict[force_side] and handle == False:
            my_dict[force_side].append(force_user)

    if '->' in forcebook:

        force_user, force_side = forcebook.split(' -> ')

        for k, v in my_dict.items():
            if force_user in v:
                v.remove(force_user)

        my_dict[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')


sorted_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for k, v in sorted_dict.items():
    if len(v) > 0:
        print(f'Side: {k}, Members: {len(v)}')
        for user in sorted(v, key=lambda name: name):
            print(f'! {user}')
