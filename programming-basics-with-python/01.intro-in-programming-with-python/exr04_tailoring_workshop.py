num_tables = int(input())
length_tables = float(input())
width = float(input())

area_tablecloth = num_tables * (length_tables +2 * 0.30) * (width + 2 * 0.30)
area_square = num_tables * (length_tables / 2) * (length_tables / 2)

price_in_usd = (area_tablecloth * 7) + (area_square * 9)
price_in_bgn = price_in_usd * 1.85

print(f'{price_in_usd:.2f} USD')
print((f'{price_in_bgn:.2f} BGN'))