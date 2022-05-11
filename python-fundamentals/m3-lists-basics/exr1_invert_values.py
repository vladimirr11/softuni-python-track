string = input().split()

result = []

for item in string:
    if int(item) > 0:
        result.append(int(item) * -1)
    if int(item) < 0:
        result.append(int(item[1:]))
    if int(item) == 0:
        result.append(int(item))

print(result)
