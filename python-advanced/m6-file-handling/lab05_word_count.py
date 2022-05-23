import re


def get_words(file_path):
    with open(file_path, 'r') as file:
        return file.read().split()


def count_words(file_path, words_to_count):
    words_dict = {}
    for word in words_to_count:
        if word not in words_dict:
            words_dict[word] = 0

    with open(file_path, 'r') as file:
        words = []
        for line in file:
            words_of_line = re.findall(r'[A-Za-z]+', line)
            words.append(words_of_line)

        lower_case_words = [word.lower() for row in words for word in row]

    for word in lower_case_words:
        if word in words_dict:
            words_dict[word] += 1

    return words_dict


def print_sorted_counted_words(words_dict):
    sorted_dict = dict(
        sorted(words_dict.items(), key=lambda pair: (pair[1], pair[0]), reverse=True))
    for k, v in sorted_dict.items():
        print(f'{k} - {v}')


file_path_get_words = './06-File-Handling-Lab-Resources/Words Count/words.txt'
file_path_count_words = './06-File-Handling-Lab-Resources/Words Count/text.txt'

words = get_words(file_path_get_words)
print_sorted_counted_words(count_words(file_path_count_words, words))
