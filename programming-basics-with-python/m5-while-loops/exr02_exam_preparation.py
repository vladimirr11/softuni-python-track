num_poor_marks = int(input())

counter = 0
score = 0
unsatisfied_result = 0
has_failed = True
last_name = ''

while unsatisfied_result < num_poor_marks:
    task_name = input()
    if task_name == 'Enough':
        has_failed = False
        break

    task_mark = int(input())
    if task_mark <= 4:
        unsatisfied_result += 1
    score += task_mark
    counter += 1
    last_name = task_name


if has_failed:
    print(f'You need a break, {num_poor_marks} poor grades.')
else:
    print(f"Average score: {score/counter:.2f}")
    print(f"Number of problems: {counter}")
    print(f"Last problem: {last_name}")
