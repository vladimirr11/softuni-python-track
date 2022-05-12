old_version = list(map(int, input().split('.')))

if old_version[2] < 9:
    old_version[2] += 1

if old_version[2] == 9:
    old_version[2] = 0
    if old_version[1] < 9:
        old_version[1] += 1
    else:
        old_version[1] = 0
        old_version[0] += 1

print('.'.join(list(map(str, old_version))))
