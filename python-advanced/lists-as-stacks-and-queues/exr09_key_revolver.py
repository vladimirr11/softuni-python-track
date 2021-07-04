price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = [int(x) for x in input().split()]
value_of_intelligence = int(input())


counter = 0
while bullets:
    counter += 1
    current_bullet = bullets.pop()
    if current_bullet <= locks[0]:
        print('Bang!')
        if counter % gun_barrel_size == 0 and len(locks) >= 1 and len(bullets) > 0:
            print('Reloading!')

        del locks[0]

        if not locks:
            print(f'{len(bullets)} bullets left. Earned ${value_of_intelligence - (counter * price_of_bullet)}')
            break
    else:
        print('Ping!')
        if counter % gun_barrel_size == 0 and len(bullets) > 0:
            print('Reloading!')

        if not bullets:
            print(f'Couldn\'t get through. Locks left: {len(locks)}')
