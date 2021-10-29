import os

while True:
    command = input().split('-')

    if command[0] == 'End':
        break

    elif command[0] == 'Create':
        file_name = command[1]
        with open(file_name, 'w') as file:
            file.write('')
        
    elif command[0] == 'Add':
        file_name, content = command[1], command[2]
        with open(file_name, 'a') as file:
            file.write(content + '\r\n')
    
    elif command[0] == 'Replace':
        file_name, old_str, new_str = command[1], command[2], command[3]
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                content = file.read()

            content = content.replace(old_str, new_str)
            with open(file_name, 'w') as file:
                file.write(content)
        else:
            print('An error occured')
    
    elif command[0] == 'Delete':
        file_name = command[1]
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occured')
            