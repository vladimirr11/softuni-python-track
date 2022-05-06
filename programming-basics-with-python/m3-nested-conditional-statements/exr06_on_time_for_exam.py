import math

hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

hour_exam = 60 * hour_of_exam
minutes_exam = minutes_of_exam + hour_exam

hour_arrival = 60 * hour_of_arrival
minutes_arrival = minutes_of_arrival + hour_arrival

if minutes_arrival > minutes_exam:
    late = minutes_arrival - minutes_exam
    if late < 60:
        print('Late')
        print(f'{late} minutes after the start')
    elif late >= 60:
        exact_hour = math.floor(late / 60)
        exact_min = late % 60
        print('Late')
        print(f'{exact_hour}:{exact_min:02} hours after the start')

elif minutes_arrival == minutes_exam:
    print('On time')

elif minutes_exam > minutes_arrival:
    late = minutes_exam - minutes_arrival
    if late <= 30:
        print('On time')
        print(f'{late} minutes before the start')
    elif 30 < late < 60:
        print('Early')
        print(f'{late} minutes before the start')
    elif late >= 60:
        exact_hour = math.floor(late / 60)
        exact_min = late % 60
        print('Early')
        print(f'{exact_hour}:{exact_min:02} hours before the start')
