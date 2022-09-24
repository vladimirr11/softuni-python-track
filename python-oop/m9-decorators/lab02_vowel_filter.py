def vowel_filter(func):
    def wrapper():
        result = func()
        vowels = 'aeiouy'
        return [let for let in result if let in vowels]
    
    return wrapper


if __name__ == '__main__':
    @vowel_filter
    def get_letters():
        return ['a', 'b', 'c', 'd', 'e']

    print(get_letters())
