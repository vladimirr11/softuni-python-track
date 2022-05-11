string = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

HANDLE = False

for item in string:
    team, number = item.split('-')
    number = int(number)

    if team == 'A':
        if number not in team_a:
            continue
        team_a.remove(number)
        if len(team_a) < 7:
            HANDLE = True
            break

    if team == 'B':
        if number not in team_b:
            continue
        team_b.remove(number)
        if len(team_b) < 7:
            HANDLE = True
            break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')

if HANDLE == True:
    print('Game was terminated')
