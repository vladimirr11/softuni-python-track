import os

def sort_dict(dictionary):
    """
    """
    return dict(sorted(dictionary.items(), key=lambda name: name))


def traverse_directory(path):
    """
    """
    files_dict = {}
    for root, _, files in os.walk(path):
        num_separators = path.count(os.path.sep)
        if num_separators - root.count(os.path.sep) > 1:
            continue
        for file in files:
            extension = file.split('.')[-1]
            if extension not in files_dict:
                files_dict[extension] = []
            files_dict[extension].append(file)
    
    return sort_dict(files_dict)


def get_sorted_files(sorted_files_dict):
    """
    """
    result = ''
    for k, v in sorted_files_dict.items():
        result += f'.{k}\r\n'
        for file in v:
            result += f'- - - {file}\r\n'

    return result


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Работен плот')
final_location = desktop + os.path.sep + 'report.txt'

result = get_sorted_files(traverse_directory(input()))

with open(final_location, 'w') as f:
    f.write(result)
