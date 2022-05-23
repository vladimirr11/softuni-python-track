def create_ascii_dict(chars: str):
    characters = chars.split(', ')
    char_ascii_dict = {char: ord(char) for char in characters}

    return char_ascii_dict


print(create_ascii_dict(input()))
