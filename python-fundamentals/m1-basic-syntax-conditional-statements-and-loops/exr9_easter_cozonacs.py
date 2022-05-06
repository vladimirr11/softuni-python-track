budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75

milk_price = (flour_price * 1.25) / 4

money_needed_for_cozonac = flour_price + eggs_price + milk_price

colored_eggs = 0
cozonacs = 0

while budget > 0:
    budget -= money_needed_for_cozonac
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        colored_eggs -= cozonacs - 2
    if budget < money_needed_for_cozonac:
        break

print(f'You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
