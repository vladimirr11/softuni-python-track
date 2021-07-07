def print_unique_username(num):
    """
    """
    usernames = set()
    for _ in range(num):
        username = input()
        usernames.add(username)

    [print(user) for user in usernames]


print_unique_username(int(input()))
