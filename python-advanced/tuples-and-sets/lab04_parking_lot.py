def get_input(num_in_out_cars):
    """
    """
    return [input().split(', ') for _ in range(num_in_out_cars)]


def record_parking_lot(in_out_cars):
    """"
    """
    entered_car = set()
    left_cars = set()

    for car in in_out_cars:
        if car[0] == 'IN':
            if car[1] in left_cars:
                left_cars.remove(car[1])
            entered_car.add(car[1])
        else:
            left_cars.add(car[1])
    
    return [print(car) for car in entered_car.difference(left_cars)] \
        if entered_car.difference(left_cars) else print(f'Parking Lot is Empty')  


record_parking_lot(get_input(int(input())))
