input_text = input()

letters_dict = {}
for letter in input_text:
    if letter not in letters_dict:
        letters_dict[letter] = 0
    letters_dict[letter] += 1


sorted_letter_dict = dict(sorted(letters_dict.items()))

for k, v in sorted_letter_dict.items():
    print(f'{k}: {v} time/s')
