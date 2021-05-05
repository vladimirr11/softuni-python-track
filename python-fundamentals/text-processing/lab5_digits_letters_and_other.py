text = input()


def get_all_digits(text):
    """"
    Take out all digits from given text.
    """
    return get_all_character_matching_condition(text, lambda char: char.isdigit())


def get_all_letters(text):
    """"
    Take out all letters from given text.
    """
    return get_all_character_matching_condition(text, lambda char: char.isalpha())


def get_all_other_characters(text):
    """"
    Take out all non-numeric and all non-alphabetic character from given text.
    """
    return get_all_character_matching_condition(text, lambda char: not char.isdigit() and not char.isalpha())


def get_all_character_matching_condition(text, condition):
    """
    Take out all character provided given condition.
    """
    result = ''

    for char in text:
        if condition(char):
            result += char
    
    return result


print(get_all_digits(text))
print(get_all_letters(text))
print(get_all_other_characters(text))