elements = input().split(' ')

# products = {}

# for index in range(0, len(elements), 2):
#     product_name = elements[index]
#     product_values = elements[index + 1]
#     products[product_name] = int(product_values)

# print(products)

products = {elements[index]: int(elements[index + 1]) for index in range(0, len(elements), 2)}

print(products)