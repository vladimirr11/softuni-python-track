student_name = input()

marks_for_each_grade = 0
grade = 1

while grade <= 12:
    mark = float(input())
    if mark < 4.00:
        continue

    marks_for_each_grade += mark
    grade += 1

average_grade = marks_for_each_grade / 12
print(f'{student_name} graduated. Average grade: {average_grade:.2f}')