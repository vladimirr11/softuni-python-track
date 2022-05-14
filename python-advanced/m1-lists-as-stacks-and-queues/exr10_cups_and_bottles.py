from collections import deque


cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))

wasted_water = 0
no_bottles_flag = False

while cups:
    if bottles:
        cup = cups.popleft()
        bottle = bottles.pop()

        if bottle >= cup:
            wasted_water += bottle - cup
        else:
            cup -= bottle
            if cup > 0:
                while True:
                    if bottles:
                        new_bottle = bottles.pop()
                        if new_bottle < cup:
                            cup -= new_bottle
                            continue
                        else:
                            wasted_water += new_bottle - cup
                            break
                    else:
                        no_bottles_flag = True
                        break
    else:
        no_bottles_flag = True
        break


if no_bottles_flag:
    print(f'Cups: {" ".join([str(cup) for cup in cups])}\nWasted litters of water: {wasted_water}')
else:
    print(f'Bottles: {" ".join([str(bottle) for bottle in bottles])}\nWasted litters of water: {wasted_water}')
