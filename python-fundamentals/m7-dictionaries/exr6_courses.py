courses_dict = {}

while True:
    courses_input = input()
    if courses_input == 'end':
        break

    course_name, student = courses_input.split(' : ')

    if course_name not in courses_dict:
        courses_dict[course_name] = []

    courses_dict[course_name].append(student)

sorted_dict = dict(sorted(courses_dict.items(),
                   key=lambda x: len(x[1]), reverse=True))

for k, v in sorted_dict.items():
    print(f'{k}: {len(v)}')
    for name in sorted(v, key=lambda name: name):
        print(f'-- {name}')
