from collections import deque


num_pumps = int(input())

fuel = 0

pumps = deque()
for _ in range(num_pumps):
    pump = [int(i) for i in input().split()]
    pumps.append(pump)


def get_petrol(num_pumps, pumps: deque, fuel):
    """
    """
    for i in range(num_pumps):
        is_valid = True
        fuel = 0

        for _ in range(num_pumps):
            current_pump = pumps.popleft()
            fuel += current_pump[0] - current_pump[1]

            if fuel < 0:
                is_valid = False
                fuel = 0 
                
            pumps.append(current_pump)
        
        if is_valid:
            print(i)
            break
        
        pumps.append(pumps.popleft())


get_petrol(num_pumps, pumps, fuel)
