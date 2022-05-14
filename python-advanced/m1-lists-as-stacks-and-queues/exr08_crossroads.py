from collections import deque

duration_green_light = int(input())
duration_free_window = int(input())

flag = True
traffic_counter = 0

queue = deque()
while True:
    green_light = duration_green_light
    free_window = duration_free_window

    command = input()
    if command == 'END':
        break
    elif command == 'green':
        while queue:
            car = queue.popleft()
            if len(car) <= green_light:
                traffic_counter += 1
                green_light -= len(car)
            else:
                if green_light + free_window >= len(car):
                    traffic_counter += 1
                    break
                else:
                    idx_hitted_char = (green_light + free_window)
                    print(f'A crash happened!\n{car} was hit at {car[idx_hitted_char]}.')
                    flag = False
                    break
    elif flag == False:
        break
    else:
        queue.append(command)


if flag:
    print(f'Everyone is safe.\n{traffic_counter} total cars passed the crossroads.')
