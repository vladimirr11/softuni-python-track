desired_expirience = int(input())
num_of_battles = int(input())

counter = 0
total_expirience = 0
handle = False

for i in range(1, num_of_battles + 1):
    battle_expirience = int(input())
    counter += 1

    if i % 3 == 0:
        total_expirience += battle_expirience * 1.15
    elif i % 5 == 0 and i % 15 == 0:
        total_expirience += battle_expirience * 1.05
    elif i % 5 == 0:
        total_expirience += battle_expirience * 0.9
    else:
        total_expirience += battle_expirience

    if total_expirience >= desired_expirience:
        handle = True
        break

if handle:
    print(f'Player successfully collected his needed experience for {counter} battles.')
else:
    print(f'Player was not able to collect the needed experience, {desired_expirience - total_expirience:.2f} more needed.')
