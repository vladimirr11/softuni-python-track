user_names = input().split(', ')

for user in user_names:
    if not (3 < len(user) < 16):
        continue
    
    is_valid = True

    for ch in user:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            is_valid = False
            break
    
    if not is_valid:
        continue

    print(user)