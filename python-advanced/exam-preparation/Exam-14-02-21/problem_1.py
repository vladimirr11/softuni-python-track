from collections import deque

firework_effects = deque(map(int, input().split(', ')))
explosives = deque(map(int, input().split(', ')))

palm_firework = 0
willow_firework = 0
crossette_firework = 0

success = False

while firework_effects and explosives:
    curr_firework = firework_effects.popleft()
    curr_explosive = explosives.pop()

    if curr_explosive <= 0:
        del curr_explosive
        firework_effects.appendleft(curr_firework)
        continue
    
    if curr_firework <= 0:
        del curr_firework
        explosives.append(curr_explosive)
        continue

    if (curr_firework + curr_explosive) % 3 == 0 and (curr_firework + curr_explosive) % 5 == 0:
        crossette_firework += 1
        del curr_firework
        del curr_explosive
    
    elif (curr_firework + curr_explosive) % 3 == 0:
        palm_firework += 1
        del curr_firework
        del curr_explosive
    
    elif (curr_firework + curr_explosive) % 5 == 0:
        willow_firework += 1
        del curr_firework
        del curr_explosive

    else:
        curr_firework -= 1
        firework_effects.append(curr_firework)
        explosives.append(curr_explosive)
    
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        success = True
        break


if success:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f'Sorry. You can\'t make the perfect firework show.')

if firework_effects:
    firework_effects = list(firework_effects)
    print(f'Firework Effects left: {", ".join([str(fw) for fw in firework_effects])}')

if explosives:
    explosives = list(explosives)
    print(f'Explosive Power left: {", ".join([str(ep) for ep in explosives])}')


print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_firework}')
