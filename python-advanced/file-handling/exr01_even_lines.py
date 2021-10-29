def reverse_even_line_words(file_path, mode):
    """"
    """
    with open(file_path, mode) as file:
        for idx, line in enumerate(file):
            if idx % 2 == 0:
                for el in line:
                    if el in '-,.!?':
                        line = line.replace(el, '@')
                        
                line_words = line.split()
                rev_line_words = line_words[::-1]
                print(' '.join(rev_line_words))


file_path = './exr01_text.txt'
mode = 'r'

reverse_even_line_words(file_path, mode)
