def filter_even_lenght_words(words):
    """
    """
    return [print(word) for word in words.split() if len(word) % 2 == 0]

    
filter_even_lenght_words(input())
