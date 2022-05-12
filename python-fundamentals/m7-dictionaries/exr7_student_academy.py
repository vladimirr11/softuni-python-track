number_of_students = int(input())

students_dict = {}

for _ in range(number_of_students):
    student_name = input()
    grade = float(input())

    if student_name not in students_dict:
        students_dict[student_name] = []

    students_dict[student_name].append(grade)


best_students_dict = dict(filter(lambda x: sum(
    x[1]) / len(x[1]) >= 4.5, students_dict.items()))

sorted_dict = dict(sorted(best_students_dict.items(),
                   key=lambda x: sum(x[1]) / len(x[1]), reverse=True))

for k, v in sorted_dict.items():
    print(f'{k} -> {sum(v) / len (v):.2f}')
