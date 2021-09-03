def filter_vowels_from_text(text):
    """
    """
    vowels = ['a', 'o', 'u', 'e', 'i']
    text_without_vowels = [char for char in text if char not in vowels]

    return ''.join(text_without_vowels)


print(filter_vowels_from_text(input()))
