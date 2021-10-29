import os
from os import remove

file_path = './06-File-Handling-Lab-Resources/my_first_file.txt'

try:
    os.path.exists(file_path)
    remove(file_path)
    print('File removed!')
except:
    print('File already deleted!')
    