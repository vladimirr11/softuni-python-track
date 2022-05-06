number_of_snowballs = int(input())

max_snowball_value = 0
max_snow_quantity = 0
max_snowball_time = 0
max_snowball_quality = 0

for snowball in range(number_of_snowballs):
    snow_quantity = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int(snow_quantity / snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snow_quantity = snow_quantity
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality


print(f'{max_snow_quantity} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})')
