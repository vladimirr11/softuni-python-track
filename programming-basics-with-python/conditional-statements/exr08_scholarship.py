income = float(input())
average_success = float(input())
min_wage = float(input())

social_scholarship = 0.35 * min_wage
excellent_scholarship = average_success * 25

if 4.50 < average_success < 5.50 and min_wage > income:
    print(f'You get a Social scholarship {social_scholarship:.0f} BGN')
elif 4.50 < average_success < 5.50 and min_wage < income:
    print('You cannot get a scholarship!')
elif average_success >= 5.50 and social_scholarship > excellent_scholarship:
    print(f'You get a Social scholarship {social_scholarship:.0f} BGN')
elif average_success >= 5.50 and social_scholarship < excellent_scholarship:
    print(f'You get a scholarship for excellent results {excellent_scholarship:.0f} BGN')
elif average_success >= 5.50 and social_scholarship == excellent_scholarship:
    print(f'You get a scholarship for excellent results {excellent_scholarship:.0f} BGN')
else:
    print('You cannot get a scholarship!')
