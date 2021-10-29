try:
    with open('./06-File-Handling-Lab-Resources/File Opener/text.txt', 'r') as file:
        if file:
            print('File found')
except:
    print('File not found')
    