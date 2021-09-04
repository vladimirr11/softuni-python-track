def flatten_lists(string):
    """
    """
    lst = [[int(x) for x in chars.replace(' ', '')] for chars in string.split('|')]
    
    return [[print(l, end=' ') for l in sub_lst] for sub_lst in lst[::-1]]


flatten_lists(input())
