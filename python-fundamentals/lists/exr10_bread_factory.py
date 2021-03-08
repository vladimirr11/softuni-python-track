events = input().split('|')

initial_energy = 100
initial_coins = 100

HANDLE = False

for event in events:
    event_ingredient, number = event.split('-')
    number = int(number)

    if event_ingredient == 'rest':
        if number + initial_energy > 100:
            print('You gained 0 energy.')
            print(f'Current energy: {initial_energy}.')
        elif 0 < number + initial_energy < 100:
            initial_energy += number
            print(f'You gained {number} energy.')
            print(f'Current energy: {initial_energy}.')
        
    elif event_ingredient == 'order':
        initial_energy -= 30

        if initial_energy >= 0:
            initial_coins += number
            print(f'You earned {number} coins.')
        if initial_energy < 0:
            initial_energy += 50
            print('You had to rest!')
        
        
    elif initial_coins >= 0:
        initial_coins -= number
        if initial_coins >= 0:
            print(f'You bought {event_ingredient}.')
    
        if initial_coins < 0:
            print(f'Closed! Cannot afford {event_ingredient}.')
            HANDLE = True
            break


if not HANDLE == True:
    print(f'Day completed!\nCoins: {initial_coins}\nEnergy: {initial_energy}')