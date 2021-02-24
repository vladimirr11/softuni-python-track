num_deposit = int(input())

deposit_made = 0
stacked_money = 0
number_deposit = 0

while number_deposit < num_deposit:
    deposit_made = float(input())
    if deposit_made <= 0:
        print(f'Invalid operation!')
        break

    print(f'Increase: {deposit_made:.2f}')
    stacked_money += deposit_made
    number_deposit += 1

print(f'Total: {stacked_money:.2f}')