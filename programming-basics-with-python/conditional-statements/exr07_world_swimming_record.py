record = float(input())
distance = float(input())
time_for_metre = float(input())

total_time = distance * time_for_metre
lag = (distance // 15) * 12.5
total_time += lag

if record > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    difference = total_time - record
    print(f'No, he failed! He was {difference:.2f} seconds slower.')