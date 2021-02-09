square_meters_planted = float(input())

costs = square_meters_planted * 7.61
discount = (costs * 18) / 100
total_sum = costs - discount

print (f'The final price is: {total_sum:.2f} lv.')
print (f'The discount is: {discount:.2f} lv.')