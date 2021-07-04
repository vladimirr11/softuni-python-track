from collections import deque


robot_info = input().split(';')
time = [int(x) for x in input().split(':')]

available_robots = deque()
waiting_robots = deque()
products = deque()
robot_dict = {}


def next_second(h, m, s):
    """
    """
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    
    return h, m, s


def get_processing_time(robot_info: list, available_robots: deque, 
                        waiting_robots: deque, products: deque, 
                        robot_dict: dict, time: list):
    """
    """

    product = input()
    while product != 'End':
        products.append(product)
        product = input()


    for robot in robot_info:
        robot_name = robot.split('-')[0]
        robot_time = int(robot.split('-')[1])
        available_robots.append([robot_name, robot_time])
        robot_dict[robot_name] = robot_time


    while products:
        for robot in waiting_robots:
            robot_name = robot[0]
            robot[1] -= 1
            if robot[1] <= 0:
                available_robots.append([robot_name, robot_dict[robot_name]])

        waiting_robots = [r for r in waiting_robots if r[1] > 0]

        time = next_second(time[0], time[1], time[2])

        current_product = products.popleft()

        if not available_robots:
            products.append(current_product)
            continue

        current_robot = available_robots.popleft()

        print(f'{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]')

        waiting_robots.append(current_robot)


get_processing_time(robot_info, available_robots, waiting_robots, products, robot_dict, time)
