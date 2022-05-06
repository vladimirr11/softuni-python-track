student_name = input()

marks_for_each_grade = 0
grade = 1
fails = 1

while grade <= 12:
    mark = float(input())
    if mark < 4.00:
        mark = float(input())
        fails += 1
        if fails == 2:
            break

    grade += 1
    marks_for_each_grade += mark

average_grade = marks_for_each_grade / 12

if fails == 2:
    print(f'{student_name} has been excluded at {grade} grade')
else:
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
