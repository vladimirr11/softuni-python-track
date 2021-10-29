try:
    with open('./06-File-Handling-Lab-Resources/my_first_file.txt', 'w') as file:
        file.write('I just created my first file!')
except:
    print('Error!')
    