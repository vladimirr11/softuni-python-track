def age_assignment(*args, **kwargs):
    """
    """
    name_age_dict = {}
    for name in args:
        if name[0] in kwargs and name not in name_age_dict:
            name_age_dict[name] = kwargs[name[0]]

    return name_age_dict


print(age_assignment('Peter', 'George', G=26, P=19))
print(age_assignment('Amy', 'Bill', 'Willy', W=36, A=22, B=61))
