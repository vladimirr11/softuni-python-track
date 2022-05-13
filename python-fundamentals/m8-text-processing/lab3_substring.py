def replace_all(string_to_replace, actual_string):
    """
    Replace all the occurrances of given string in another specified string.
    """
    while string_to_replace in actual_string:
        actual_string = actual_string.replace(string_to_replace, '')

    return actual_string


print(replace_all(input(), input()))
