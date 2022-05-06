num_days = int(input())
service = input()
evaluation = input()

nights = num_days - 1
sum_without_disc = 0
disc = 0
end_sum = 0

if num_days < 11:
    if service == 'room for one person':
        sum_without_disc = nights * 18
    elif service == 'apartment':
        sum_without_disc = nights * 25
        disc = sum_without_disc * 0.3
        end_sum = sum_without_disc - disc
    elif service == 'president apartment':
        sum_without_disc = nights * 35
        disc = sum_without_disc * 0.1
        end_sum = sum_without_disc - disc
elif 11 < num_days < 15:
    if service == 'room for one person':
        sum_without_disc = nights * 18
    elif service == 'apartment':
        sum_without_disc = nights * 25
        disc = sum_without_disc * 0.35
        end_sum = sum_without_disc - disc
    elif service == 'president apartment':
        sum_without_disc = nights * 35
        disc = sum_without_disc * 0.15
        end_sum = sum_without_disc - disc
elif num_days > 15:
    if service == 'room for one person':
        sum_without_disc = nights * 18
    elif service == 'apartment':
        sum_without_disc = nights * 25
        disc = sum_without_disc * 0.5
        end_sum = sum_without_disc - disc
    elif service == 'president apartment':
        sum_without_disc = nights * 35
        disc = sum_without_disc * 0.20
        end_sum = sum_without_disc - disc


if evaluation == 'positive' and service == 'room for one person':
    sum_without_disc += (sum_without_disc * 0.25)
    print(f'{sum_without_disc:.2f}')
elif evaluation == 'negative' and service == 'room for one person':
    sum_without_disc += (sum_without_disc * 0.10)
    print(f'{sum_without_disc:.2f}')
elif evaluation == 'positive' and service == 'apartment':
    end_sum += (end_sum * 0.25)
    print(f'{end_sum:.2f}')
elif evaluation == 'negative' and service == 'apartment':
    end_sum += (end_sum * 0.10)
    print(f'{end_sum:.2f}')
elif evaluation == 'positive' and service == 'president apartment':
    end_sum += (end_sum * 0.25)
    print(f'{end_sum:.2f}')
elif evaluation == 'negative' and service == 'president apartment':
    end_sum -= (end_sum * 0.10)
    print(f'{end_sum:.2f}')
