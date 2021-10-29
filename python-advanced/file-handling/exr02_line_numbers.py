def manipulate_txt_file(file_path):
    """
    """
    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            letters = len([l for l in line if l.isalpha()])
            punctuation_marks = '.?!",\';:-'
            punct_marks_counter = 0
            for char in line:
                if char in punctuation_marks:
                    punct_marks_counter += 1
            print(f'Line {idx + 1}: {line[:-1]} ({letters})({punct_marks_counter})')


path = './exr01_text.txt'

manipulate_txt_file(path)
