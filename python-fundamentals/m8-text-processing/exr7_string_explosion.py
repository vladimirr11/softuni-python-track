string = input()

index = 0
strenght = 0
result = ''

while index < len(string):
    if string[index] != '>':
        result += string[index]
        index += 1
    else:
        result += '>'
        index += 1
        strenght += int(string[index])

        while strenght > 0 and string[index] != '>':
            index += 1
            strenght -= 1

            if index >= len(string):
                break


print(result)
