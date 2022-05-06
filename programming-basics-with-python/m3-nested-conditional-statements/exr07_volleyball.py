import math

year_type = input()
num_holiday = int(input())
num_weekends_home_town = int(input())

if year_type == 'normal':
    plays_in_sofia = ((48 - num_weekends_home_town) * 3) / 4
    plays_on_holidays = (num_holiday * 2) / 3
    total_plays = plays_in_sofia + plays_on_holidays + num_weekends_home_town
    print(math.floor(total_plays))
elif year_type == 'leap':
    plays_in_sofia = (48 - num_weekends_home_town) * 3/4
    plays_on_holidays = num_holiday * 2/3
    total_plays = plays_in_sofia + plays_on_holidays + num_weekends_home_town
    add_plays = total_plays + (total_plays * 0.15)
    print(math.floor(add_plays))
