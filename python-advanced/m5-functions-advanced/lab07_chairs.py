names = input().split(', ')
size = int(input())


def people_combinations(names: list, size, result = []):
    if len(result) == size:
        print(', '.join(result))
        return
    else:
        for i in range(len(names)):
            result.append(names[i])
            people_combinations(names[i + 1:], size)
            result.pop()


people_combinations(names, size)
