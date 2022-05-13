first_employee_people = int(input())
second_employee_people = int(input())
third_employee_people = int(input())

total_people = int(input())

success_rate_per_hour = first_employee_people + \
    second_employee_people + third_employee_people
counter = 0

for hour in range(10000):
    if hour % 4 == 0:
        counter += 1
        continue
    else:
        total_people -= success_rate_per_hour

        if total_people <= 0:
            break

        counter += 1


print(f'Time needed: {counter}h.')
