def make_students_grades_dict():
    """
    """
    my_students_grades_dict = {}

    num_students = int(input())

    for _ in range(num_students):
        student_name, grades = input().split()
        if student_name not in my_students_grades_dict:
            my_students_grades_dict[student_name] = []
            my_students_grades_dict[student_name].append(grades)
        else:
            my_students_grades_dict[student_name].append(grades)
    
    return my_students_grades_dict


def average_grades(values):
    """
    """
    return sum(values) / len(values)


def format_output_students_grades(students_grades_dict):
    """
    """
    for (student, grades) in students_grades_dict.items():
        avg_grade = average_grades([float(grade) for grade in grades])
        grades = ' '.join(f'{float(grade):.2f}' for grade in grades)
        print(f'{student} -> {grades} (avg: {avg_grade:.2f})')


format_output_students_grades(make_students_grades_dict())
