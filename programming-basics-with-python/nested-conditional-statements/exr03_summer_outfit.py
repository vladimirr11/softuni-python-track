degrees = int(input())
part_of_the_day = input().capitalize()

outfit = ''
shoes = ''

if 10 <= degrees <= 18 and part_of_the_day == 'Morning':
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
elif 10 <= degrees <= 18 and part_of_the_day == 'Afternoon':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif 10 <= degrees <= 18 and part_of_the_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif 18 < degrees <= 24 and part_of_the_day == 'Morning':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif 18 < degrees <= 24 and part_of_the_day == 'Afternoon':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif 18 <= degrees <= 24 and part_of_the_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'
elif degrees > 24 and part_of_the_day == 'Morning':
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif degrees > 24 and part_of_the_day == 'Afternoon':
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
elif degrees > 24 and part_of_the_day == 'Evening':
    outfit = 'Shirt'
    shoes = 'Moccasins'


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")