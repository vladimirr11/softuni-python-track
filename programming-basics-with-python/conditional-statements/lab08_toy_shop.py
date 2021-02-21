holiday_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bears = int(input())
minion = int(input())
lorries = int(input())

total_sum_toys = (puzzles * 2.6) + (speaking_dolls * 3) + (teddy_bears * 4.10) + (minion * 8.20) + (lorries * 2)

num_toys = puzzles + speaking_dolls + teddy_bears + minion + lorries

if num_toys >= 50:
    money_after_discount = total_sum_toys * 0.75
    rent = money_after_discount * 0.1
    earned_money = money_after_discount - rent
    if earned_money >= holiday_price:
        left_money = earned_money - holiday_price
        print(f'Yes! {left_money:.2f} lv left.')
    else:
        needed_money = holiday_price - earned_money
        print(f'Not enough money! {needed_money:.2f} lv needed.')
elif num_toys < 50:
    rent = total_sum_toys * 0.1
    earned_money = total_sum_toys - rent
    needed_money = holiday_price - earned_money
    print(f'Not enough money! {needed_money:.2f} lv needed.')