intigers = list(map(str, input().split(', ')))


def get_palindrome_intigers(intigers):
    """
    """
    return True if intigers == intigers[::-1] else False


for i in intigers:
    print(get_palindrome_intigers(i))