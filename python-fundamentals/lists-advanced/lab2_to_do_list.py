tasks = []

while True:
    to_do_notes = input()
    if to_do_notes == 'End':
        break
    
    tokens = to_do_notes.split('-')
    level_of_importance = int(tokens[0])
    thinks_to_do = tokens[1]
    tasks.append((level_of_importance, thinks_to_do))

def sort_function(task):
    return task[0]

sorted_tasks = [task for task_importance, task in sorted(tasks, key = sort_function)]

print(sorted_tasks)