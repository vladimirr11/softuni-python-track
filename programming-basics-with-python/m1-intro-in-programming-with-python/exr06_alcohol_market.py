price_whiskey = float(input())
litters_beer = float(input())
litters_wine = float(input())
litters_rakia = float(input())
litters_whiskey = float(input())

price_rakia = price_whiskey / 2
price_wine = price_rakia - (0.4 * price_rakia)
price_beer = price_rakia - (0.8 * price_rakia)

sum_rakia = litters_rakia * price_rakia
sum_wine = litters_wine * price_wine
sum_beer = litters_beer * price_beer
sum_whiskey = litters_whiskey * price_whiskey

total_sum = sum_rakia + sum_wine + sum_beer + sum_whiskey

print(f'{total_sum:.2f}')
