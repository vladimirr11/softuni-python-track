file_path = input().split('\\')

last_element = file_path[-1]

file_name, file_extension = last_element.split('.')

print(f'File name: {file_name}')
print(f'File extension: {file_extension}')
