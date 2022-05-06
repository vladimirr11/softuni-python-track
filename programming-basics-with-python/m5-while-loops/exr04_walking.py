steps = input()

total_steps = 0
condition = False
steps_after_going_home = 0

while total_steps < 10000:
    if steps == 'Going home':
        steps_after_going_home = int(input())
        total_steps += steps_after_going_home
        condition = True
        break

    current_steps = int(steps)
    total_steps += current_steps
    if total_steps >= 10000:
        break
    steps = input()


diff_steps = 10000 - total_steps

if condition:
    if total_steps >= 10000:
        print(f'Goal reached! Good job!')
    else:
        print(f'{diff_steps} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
