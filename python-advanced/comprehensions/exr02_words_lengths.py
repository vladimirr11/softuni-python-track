words = input().split(', ')

def format_text(words):
    """
    """
    output = [f'{word} -> {len(word)}' for word in words]

    return output


print(', '.join(format_text(words)))
