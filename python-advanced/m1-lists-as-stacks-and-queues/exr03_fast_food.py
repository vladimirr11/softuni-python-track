def get_order(food_quantity, quantity_of_an_order):
    food_amount = food_quantity
    queue = list(map(int, quantity_of_an_order.split()))
    
    print(max(queue))

    while queue:
        index = 0
        if queue[index] <= food_amount:
            food_amount -= queue[index]
            queue.pop(index)
        else:
            left_orders = ' '.join(map(str, queue))
            print(f'Orders left: {left_orders}')
            break

    if not queue:
        print('Orders complete')


get_order(int(input()), input())
