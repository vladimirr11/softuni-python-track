emplyees_happiness = list(map(lambda x: int(x), input().split()))
happiness_factor = int(input())

increased_happiness = [ind_happiness * happiness_factor \
        for ind_happiness in emplyees_happiness]

average_happiness = sum(increased_happiness) / len(increased_happiness)

target_happiness_count = list(filter(lambda x: x >= average_happiness, increased_happiness))

if len(target_happiness_count) >= len(increased_happiness) / 2:
    print(f'Score {len(target_happiness_count)}/{len(increased_happiness)}. ' \
    'Employees are happy!')
else:
    print(f'Score {len(target_happiness_count)}/{len(increased_happiness)}. ' \
    'Employees are not happy!')