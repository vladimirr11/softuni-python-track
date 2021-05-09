price_ratings = list(map(int, input().split()))
entry_point = int(input())
type_of_items = input()
type_of_price_ratings = input()

left_array = price_ratings[:entry_point]
right_array = price_ratings[entry_point:]

entry_point_item = price_ratings[entry_point]

broken_items_left = 0
broken_items_right = 0

for el in left_array[::-1]:
    if type_of_items == 'cheap':
        if type_of_price_ratings == 'positive':
            if el < entry_point_item and el > 0:
                broken_items_left += el

        if type_of_price_ratings == 'negative': 
            if el < entry_point_item and el < 0:
                broken_items_left += el

        if type_of_price_ratings == 'all': 
            if el < entry_point_item:
                broken_items_left += el


    if type_of_items == 'expensive':
        if type_of_price_ratings == 'positive':
            if el >= entry_point_item and el > 0:
                broken_items_left += el
    
        if type_of_price_ratings == 'negative': 
                if el >= entry_point_item and el < 0:
                    broken_items_left += el
        
        if type_of_price_ratings == 'all': 
                if el >= entry_point_item:
                    broken_items_left += el


for el in right_array:
    if type_of_items == 'cheap':
        if type_of_price_ratings == 'positive':
            if el < entry_point_item and el > 0:
                broken_items_right += el

        if type_of_price_ratings == 'negative': 
            if el < entry_point_item and el < 0:
                broken_items_right += el

        if type_of_price_ratings == 'all': 
            if el < entry_point_item:
                broken_items_right += el


    if type_of_items == 'expensive':
        if type_of_price_ratings == 'positive':
            if el >= entry_point_item and el > 0:
                broken_items_right += el
    
        if type_of_price_ratings == 'negative': 
            if el >= entry_point_item and el < 0:
                broken_items_right += el
        
        if type_of_price_ratings == 'all': 
            if el >= entry_point_item:
                broken_items_right += el


if broken_items_left > broken_items_right:
    print(f'Left - {broken_items_left}')

if broken_items_left == broken_items_right:
    print(f'Left - {broken_items_left}')

if broken_items_left < broken_items_right:
    print(f'Right - {broken_items_right}')